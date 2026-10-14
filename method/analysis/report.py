"""Daily report over the data branch.

    python -m method.analysis.report --data data --out analysis/daily [--since YYYY-MM-DD]

Writes <out>/<today>/: coverage.csv, matches.csv, compare.csv, compare_summary.csv,
calibration.csv, news_events.csv, news_joined.csv, summary.md, and refreshes
<out>/latest.md.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

from .calib import add_pinnacle_close, calibration_by_sport, settled_contracts
from .compare import compare_winners, pinnacle_fair, summarize_compare
from .load import load_bbo, load_histories, load_markets, load_news, load_pinnacle, load_quota
from .match import match_events, pin_event_table, pm_event_table
from .newsjoin import join_news_to_paths, news_events


def coverage(bbo: pd.DataFrame, markets: pd.DataFrame, pin: pd.DataFrame, histories: list[dict],
             news: dict[str, list[dict]]) -> pd.DataFrame:
    rows = []
    if not bbo.empty:
        for sport, g in bbo.groupby("sport"):
            rows.append({"source": "polymarket_bbo", "sport": sport, "rows": int(len(g)),
                         "events": int(g["event_id"].nunique()), "passes": int(g["ts"].nunique()),
                         "window_rows": int((g["pass_scope"] == "window").sum()),
                         "first": g["ts"].min(), "last": g["ts"].max()})
    if not pin.empty:
        for sport, g in pin.groupby("sport"):
            rows.append({"source": "pinnacle", "sport": sport, "rows": int(len(g)),
                         "events": int(g["event_id"].nunique()), "passes": int(g["ts"].nunique()),
                         "first": g["ts"].min(), "last": g["ts"].max()})
    if histories:
        h = pd.DataFrame([{"sport": d["sport"], "settled": d.get("settlement") is not None, "n": d.get("n_points", 0)} for d in histories])
        for sport, g in h.groupby("sport"):
            rows.append({"source": "polymarket_history", "sport": sport, "rows": int(len(g)),
                         "events": int(g["settled"].sum()), "passes": int(g["n"].sum())})
    for k, docs in news.items():
        if docs:
            rows.append({"source": f"news_{k}", "sport": k.split("_")[0], "rows": int(len(docs))})
    return pd.DataFrame(rows)


def run(data: Path, out: Path, since: str | None = None, today: str | None = None) -> dict:
    today = today or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    dest = out / today
    dest.mkdir(parents=True, exist_ok=True)

    bbo = load_bbo(data, since)
    markets = load_markets(data, since)
    pin = load_pinnacle(data, since)
    histories = load_histories(data, since)
    news = load_news(data, since)
    quota = load_quota(data)

    cov = coverage(bbo, markets, pin, histories, news)
    cov.to_csv(dest / "coverage.csv", index=False)

    pm_ev, pin_ev = pm_event_table(markets), pin_event_table(pin)
    matches = match_events(pm_ev, pin_ev)
    matches.to_csv(dest / "matches.csv", index=False)
    fair = pinnacle_fair(pin)

    cmp = compare_winners(bbo, markets, fair, matches)
    cmp.to_csv(dest / "compare.csv", index=False)
    cmp_sum = summarize_compare(cmp)
    cmp_sum.to_csv(dest / "compare_summary.csv", index=False)

    settled = add_pinnacle_close(settled_contracts(histories), fair, matches)
    settled.to_csv(dest / "settled.csv", index=False)
    calib = calibration_by_sport(settled)
    calib.to_csv(dest / "calibration.csv", index=False)

    ev = news_events(news)
    ev.to_csv(dest / "news_events.csv", index=False)
    joined = join_news_to_paths(ev, histories, fair, matches, pm_ev)
    joined.to_csv(dest / "news_joined.csv", index=False)

    md = render(today, cov, pm_ev, pin_ev, matches, cmp_sum, cmp, settled, calib, ev, joined, quota)
    (dest / "summary.md").write_text(md)
    (out / "latest.md").write_text(md)
    stats = {"date": today, "bbo_rows": int(len(bbo)), "pinnacle_rows": int(len(pin)), "matches": int(len(matches)),
             "compare_rows": int(len(cmp)), "settled": int(len(settled)), "news_events": int(len(ev)),
             "news_joined": int(len(joined))}
    print(stats)
    return stats


COUNT_COLS = {"rows", "events", "passes", "window_rows", "n", "n_with_pinnacle", "path_points", "minutes_to_start", "bid_shares", "ask_shares"}


def _table(df: pd.DataFrame, cols: list[str], fmt: dict | None = None, limit: int = 60) -> list[str]:
    if df.empty:
        return ["(nothing yet)"]
    fmt = fmt or {}
    d = df[cols].head(limit)
    lines = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    for _, r in d.iterrows():
        cells = []
        for c in cols:
            v = r[c]
            if c in fmt and pd.notna(v):
                cells.append(fmt[c].format(v))
            elif c in COUNT_COLS and pd.notna(v):
                cells.append(f"{float(v):,.0f}")
            elif isinstance(v, float):
                cells.append("" if pd.isna(v) else f"{v:.3f}")
            elif isinstance(v, pd.Timestamp):
                cells.append(v.strftime("%m-%d %H:%M"))
            else:
                cells.append("" if v is None else str(v))
        lines.append("| " + " | ".join(cells) + " |")
    return lines


def render(today, cov, pm_ev, pin_ev, matches, cmp_sum, cmp, settled, calib, ev, joined, quota) -> str:
    L = [f"# Daily analysis {today}", ""]
    L += ["## Coverage", ""] + _table(cov, [c for c in ("source", "sport", "rows", "events", "passes", "window_rows", "first", "last") if c in cov.columns])
    if not quota.empty:
        q = quota.sort_values("ts").iloc[-1]
        L += ["", f"Odds API quota at last pass: used {q.get('quota_used')}, remaining {q.get('quota_remaining')} "
              f"({len(quota)} Pinnacle passes recorded)."]
    L += ["", "## Event matching (Polymarket US vs Pinnacle)", "",
          f"{len(pm_ev)} Polymarket events, {len(pin_ev)} Pinnacle events, {len(matches)} matched "
          f"({int((matches['how'] == 'full').sum()) if not matches.empty else 0} by full name, "
          f"{int((matches['how'] == 'nick').sum()) if not matches.empty else 0} by nickname)."]
    if not pm_ev.empty and not matches.empty:
        un = pm_ev[~pm_ev["event_id"].isin(matches["pm_event_id"])]
        if not un.empty:
            L += ["", f"Unmatched Polymarket events ({len(un)}): " + "; ".join(
                f"{r['sport']} {r['event_title']}" for _, r in un.head(15).iterrows())]
    L += ["", "## Polymarket mid vs Pinnacle fair, main winner contracts", "",
          "mid_minus_fair > 0 means Polymarket prices the team higher than Pinnacle's de-vigged price. "
          "taker_edge_at_ask = fair − ask − fee: what a taker would expect if Pinnacle were exactly right.", ""]
    L += _table(cmp_sum, ["sport", "bucket", "n", "mean_diff", "mean_abs_diff", "within_1c", "within_2c", "mean_spread",
                          "median_bid_shares", "taker_edge_mean", "taker_edge_pos_share"],
                {"within_1c": "{:.0%}", "within_2c": "{:.0%}", "taker_edge_pos_share": "{:.0%}", "median_bid_shares": "{:,.0f}"})
    if not cmp.empty:
        big = cmp.reindex(cmp["mid_minus_fair"].abs().sort_values(ascending=False).index).head(12)
        L += ["", "Largest gaps seen:", ""] + _table(big, ["sport", "team", "pin_ts", "minutes_to_start", "fair", "pm_mid", "pm_spread", "mid_minus_fair", "taker_edge_at_ask"])
    L += ["", "## Test (b): calibration of last pre-game mids (settled games)", ""]
    L += _table(calib, [c for c in ("sport", "n", "mean_mid", "win_rate", "brier_pm", "log_loss_pm", "slope", "slope_se", "intercept",
                                    "n_with_pinnacle", "brier_pm_matched", "brier_pinnacle") if c in calib.columns])
    if not settled.empty:
        L += ["", f"{len(settled)} settled main winner contracts so far; calibration is reported from 30 per sport."]
    L += ["", "## Test (a): news events and price reaction", "",
          f"{len(ev)} news events recorded; {len(joined)} joined to a Polymarket contract with a price path.", ""]
    if not ev.empty:
        by = ev.groupby(["sport", "kind"]).size().reset_index(name="n")
        L += _table(by, ["sport", "kind", "n"])
    if not joined.empty:
        cols = [c for c in ("sport", "kind", "team", "detail", "news_ts", "minutes_to_start", "contract_is_news_team", "mid_before",
                            "move_plus5", "move_plus15", "move_plus30", "pin_fair_before", "pin_fair_after", "minutes_to_within_1c")
                if c in joined.columns]
        L += ["", "Most recent joined events:", ""] + _table(joined.sort_values("news_ts", ascending=False), cols, limit=40)
    L += ["", "Generated by method/analysis/report.py from the data branch."]
    return "\n".join(L) + "\n"


def main(argv=None) -> None:
    p = argparse.ArgumentParser(prog="method.analysis.report")
    p.add_argument("--data", default="data")
    p.add_argument("--out", default="analysis/daily")
    p.add_argument("--since", default=None, help="only days >= YYYY-MM-DD")
    args = p.parse_args(argv)
    run(Path(args.data), Path(args.out), args.since)


if __name__ == "__main__":
    main()
