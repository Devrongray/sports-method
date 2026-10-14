"""Polymarket US quotes against de-vigged Pinnacle prices for matched events.

For every Pinnacle snapshot of a matched event's h2h market, take the nearest
Polymarket quote of that event's main WINNER contract within `max_gap_minutes`
and compare the contract mid with Pinnacle's fair probability for the team
the contract pays for. Totals are compared only when the lines agree.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from ..devig import devig
from ..fees import taker_fee
from .match import norm, nickname


def pinnacle_fair(pin: pd.DataFrame, method: str = "additive") -> pd.DataFrame:
    """One row per (event, ts, market, point, outcome) with fair_prob."""
    if pin.empty:
        return pd.DataFrame()
    rows = []
    keys = ["sport", "event_id", "ts", "market", "point"]
    for key, g in pin.groupby(keys, dropna=False):
        prices = g["price"].astype(float).tolist()
        if len(prices) < 2 or any(p <= 1 for p in prices):
            continue
        fair = devig(prices, method)
        for (_, r), p in zip(g.iterrows(), fair):
            rows.append({**{k: r[k] for k in keys}, "outcome": r["outcome"], "price": r["price"],
                         "fair_prob": float(p), "home": r["home"], "away": r["away"],
                         "commence_time": r["commence_time"]})
    return pd.DataFrame(rows)


def _team_fair(fair_h2h: pd.DataFrame, team_name: str) -> pd.Series | None:
    """Rows of the h2h fair table for the named team (full name or nickname)."""
    n, k = norm(team_name), nickname(team_name)
    m = fair_h2h["outcome"].map(norm) == n
    if not m.any():
        m = fair_h2h["outcome"].map(nickname) == k
    return m


def compare_winners(bbo: pd.DataFrame, markets: pd.DataFrame, fair: pd.DataFrame, matches: pd.DataFrame,
                    max_gap_minutes: float = 10.0, fee_coefficient: float = 0.0695) -> pd.DataFrame:
    """Per Pinnacle snapshot: Polymarket mid/ask vs fair for the long team."""
    if bbo.empty or markets.empty or fair.empty or matches.empty:
        return pd.DataFrame()
    main = markets[(markets["market_class"] == "WINNER") & (markets["is_main"])]
    main = main.sort_values("ts").groupby(["sport", "event_id", "market_slug"], as_index=False).last()
    q = bbo[(bbo["market_class"] == "WINNER")].dropna(subset=["mid"]).sort_values("ts")
    h2h = fair[fair["market"] == "h2h"].sort_values("ts")
    out = []
    for _, mt in matches.iterrows():
        contracts = main[(main["sport"] == mt["sport"]) & (main["event_id"] == mt["pm_event_id"])]
        pf = h2h[(h2h["sport"] == mt["sport"]) & (h2h["event_id"] == mt["pin_event_id"])]
        if contracts.empty or pf.empty:
            continue
        for _, c in contracts.iterrows():
            team = c.get("long_team_name")
            if not team:
                continue
            sel = _team_fair(pf, team)
            if sel is None or not sel.any():
                continue
            team_fair = pf[sel][["ts", "fair_prob", "price"]].rename(columns={"ts": "pin_ts"})
            quotes = q[q["market_slug"] == c["market_slug"]][["ts", "mid", "best_bid", "best_ask", "spread",
                                                              "bid_shares", "ask_shares", "minutes_to_start"]]
            if quotes.empty:
                continue
            joined = pd.merge_asof(team_fair.sort_values("pin_ts"), quotes.sort_values("ts"),
                                   left_on="pin_ts", right_on="ts", direction="nearest",
                                   tolerance=pd.Timedelta(minutes=max_gap_minutes))
            joined = joined.dropna(subset=["mid"])
            for _, j in joined.iterrows():
                fee = taker_fee(float(j["best_ask"]), fee_coefficient) if pd.notna(j["best_ask"]) and 0 < j["best_ask"] < 1 else np.nan
                out.append({
                    "sport": mt["sport"], "pm_event_id": mt["pm_event_id"], "pin_event_id": mt["pin_event_id"],
                    "team": team, "market_slug": c["market_slug"], "pin_ts": j["pin_ts"], "pm_ts": j["ts"],
                    "gap_minutes": abs((j["ts"] - j["pin_ts"]).total_seconds()) / 60,
                    "minutes_to_start": j["minutes_to_start"], "pin_price": j["price"], "fair": j["fair_prob"],
                    "pm_mid": j["mid"], "pm_bid": j["best_bid"], "pm_ask": j["best_ask"], "pm_spread": j["spread"],
                    "bid_shares": j["bid_shares"], "ask_shares": j["ask_shares"],
                    "mid_minus_fair": j["mid"] - j["fair_prob"],
                    # Edge for a taker buying at the ask, after the fee, if Pinnacle's fair were the truth
                    "taker_edge_at_ask": (j["fair_prob"] - j["best_ask"] - fee) if pd.notna(j["best_ask"]) else np.nan,
                    "match_how": mt["how"],
                })
    return pd.DataFrame(out)


def ttl_bucket(m: float) -> str:
    if pd.isna(m):
        return "unknown"
    if m <= 15:
        return "0-15 min"
    if m <= 60:
        return "15-60 min"
    if m <= 180:
        return "1-3 h"
    if m <= 720:
        return "3-12 h"
    return "12 h+"


def summarize_compare(cmp: pd.DataFrame) -> pd.DataFrame:
    if cmp.empty:
        return pd.DataFrame()
    d = cmp.copy()
    d["bucket"] = d["minutes_to_start"].map(ttl_bucket)
    g = d.groupby(["sport", "bucket"])
    s = g.agg(n=("mid_minus_fair", "size"),
              mean_diff=("mid_minus_fair", "mean"),
              mean_abs_diff=("mid_minus_fair", lambda x: x.abs().mean()),
              within_1c=("mid_minus_fair", lambda x: (x.abs() <= 0.01).mean()),
              within_2c=("mid_minus_fair", lambda x: (x.abs() <= 0.02).mean()),
              mean_spread=("pm_spread", "mean"),
              median_bid_shares=("bid_shares", "median"),
              taker_edge_mean=("taker_edge_at_ask", "mean"),
              taker_edge_pos_share=("taker_edge_at_ask", lambda x: (x > 0).mean())).reset_index()
    order = {"0-15 min": 0, "15-60 min": 1, "1-3 h": 2, "3-12 h": 3, "12 h+": 4, "unknown": 5}
    s["o"] = s["bucket"].map(order)
    return s.sort_values(["sport", "o"]).drop(columns="o")
