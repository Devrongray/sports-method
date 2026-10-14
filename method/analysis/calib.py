"""Test (b): are Polymarket US last pre-game mids calibrated, by sport?

Uses the daily price-history documents (minute-level path + settlement) for
main WINNER contracts. The settlement price (1 or 0) is the outcome. Pinnacle's
fair at its last snapshot before start, when the event is matched, gives the
side-by-side Brier score the pre-registered rule asks for.
"""
from __future__ import annotations

import pandas as pd

from ..metrics import brier, calibration_fit, log_loss
from .match import nickname, norm


def settled_contracts(histories: list[dict]) -> pd.DataFrame:
    rows = []
    for d in histories:
        if d.get("market_class") != "WINNER" or d.get("settlement") is None or not d.get("last_pregame"):
            continue
        lp = d["last_pregame"]
        if lp.get("mid") is None:
            continue
        teams = d.get("teams") or []
        long_side = next((s for s in (d.get("sides") or []) if s.get("long")), None)
        team = next((t.get("name") for t in teams if long_side and t.get("id") == long_side.get("team_id")), None)
        rows.append({"sport": d["sport"], "event_id": d["event_id"], "market_slug": d["market_slug"],
                     "start": d["start"], "team": team, "last_mid": float(lp["mid"]),
                     "last_bid": lp.get("best_bid"), "last_ask": lp.get("best_ask"),
                     "last_ts": lp.get("timestamp"), "settlement": float(d["settlement"]),
                     "n_points": d.get("n_points")})
    df = pd.DataFrame(rows)
    if not df.empty:
        df["start"] = pd.to_datetime(df["start"], utc=True, errors="coerce")
        df["y"] = (df["settlement"] >= 0.5).astype(float)
    return df


def add_pinnacle_close(settled: pd.DataFrame, fair: pd.DataFrame, matches: pd.DataFrame) -> pd.DataFrame:
    """Attach Pinnacle's last pre-start fair for the same team."""
    if settled.empty or fair.empty or matches.empty:
        settled = settled.copy()
        settled["pin_close_fair"] = float("nan")
        return settled
    h2h = fair[fair["market"] == "h2h"]
    out = []
    for _, r in settled.iterrows():
        m = matches[(matches["sport"] == r["sport"]) & (matches["pm_event_id"] == r["event_id"])]
        val = float("nan")
        if not m.empty and r["team"]:
            pf = h2h[(h2h["sport"] == r["sport"]) & (h2h["event_id"] == m.iloc[0]["pin_event_id"])]
            pf = pf[pf["ts"] <= r["start"]] if pd.notna(r["start"]) else pf
            sel = pf["outcome"].map(norm) == norm(r["team"])
            if not sel.any():
                sel = pf["outcome"].map(nickname) == nickname(r["team"])
            pf = pf[sel].sort_values("ts")
            if not pf.empty:
                val = float(pf.iloc[-1]["fair_prob"])
        out.append(val)
    settled = settled.copy()
    settled["pin_close_fair"] = out
    return settled


def calibration_by_sport(settled: pd.DataFrame, min_n: int = 30) -> pd.DataFrame:
    if settled.empty:
        return pd.DataFrame()
    rows = []
    for sport, g in settled.groupby("sport"):
        row = {"sport": sport, "n": int(len(g)), "mean_mid": g["last_mid"].mean(), "win_rate": g["y"].mean()}
        if len(g) >= min_n:
            fit = calibration_fit(g["last_mid"].to_numpy(), g["y"].to_numpy())
            row.update({"brier_pm": brier(g["last_mid"], g["y"]), "log_loss_pm": log_loss(g["last_mid"], g["y"]),
                        "slope": fit.slope, "slope_se": fit.slope_se, "intercept": fit.intercept})
            h = g.dropna(subset=["pin_close_fair"])
            if len(h) >= min_n:
                row.update({"n_with_pinnacle": int(len(h)),
                            "brier_pm_matched": brier(h["last_mid"], h["y"]),
                            "brier_pinnacle": brier(h["pin_close_fair"], h["y"])})
        rows.append(row)
    return pd.DataFrame(rows)
