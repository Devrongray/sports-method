"""Test (a) preparation: what the prices did around each news timestamp.

News events (with their own timestamps):
    NHL goalie confirmations: DailyFaceoff <side>NewsCreatedAt (the posting time)
    MLB lineups / probables: the first poll at which the change was seen
    NBA injury reports: the report's file-name time, and when it was seen

For each event we find the Polymarket contract of the team concerned (same
sport, same day, team name), take the minute-level path from the history
document, and read the mid just before the news and 5, 15 and 30 minutes
after, plus Pinnacle's fair at its last snapshot before and first after.
"""
from __future__ import annotations

import re
from datetime import datetime, timedelta, timezone

import pandas as pd

from .match import nickname, norm


def _parse_ts(s: str | None) -> datetime | None:
    if not s:
        return None
    try:
        return datetime.fromisoformat(str(s).replace("Z", "+00:00")).astimezone(timezone.utc)
    except ValueError:
        return None


def news_events(news: dict[str, list[dict]]) -> pd.DataFrame:
    rows = []
    for d in news.get("nhl", []):
        seen = _parse_ts(d.get("ts"))
        for g in d.get("games") or []:
            for side in ("home", "away"):
                created = _parse_ts(g.get(f"{side}NewsCreatedAt"))
                if not created:
                    continue
                rows.append({"sport": "nhl", "kind": f"goalie_{g.get(side + 'NewsStrengthName') or 'unknown'}".lower(),
                             "team": g.get(f"{side}TeamName"), "detail": g.get(f"{side}GoalieName"),
                             "news_ts": created, "seen_ts": seen, "game_start": _parse_ts(g.get("dateGmt")),
                             "source": g.get(f"{side}NewsSourceName")})
    for d in news.get("mlb", []):
        seen = _parse_ts(d.get("ts"))
        state = d.get("state") or {}
        for ch in d.get("changes") or []:
            g = state.get(str(ch.get("gamePk"))) or {}
            field = ch.get("field")
            if field in ("lineup_home", "probable_home"):
                team = g.get("home")
            elif field in ("lineup_away", "probable_away"):
                team = g.get("away")
            else:
                continue
            rows.append({"sport": "mlb", "kind": field, "team": team,
                         "detail": (ch.get("after") if isinstance(ch.get("after"), str) else f"{len(ch.get('after') or [])} players"),
                         "news_ts": seen, "seen_ts": seen, "game_start": _parse_ts(g.get("gameDate")), "source": "MLB StatsAPI"})
    for d in news.get("nba", []):
        seen = _parse_ts(d.get("ts"))
        m = re.search(r"Injury-Report_(\d{4}-\d{2}-\d{2})_(\d{2})_(\d{2})(AM|PM)", d.get("url") or "")
        report_ts = None
        if m:
            hh = int(m.group(2)) % 12 + (12 if m.group(4) == "PM" else 0)
            # Report times are US Eastern; EDT in October–early November, EST after. Approximate with -4h until 1 Nov.
            local = datetime.fromisoformat(f"{m.group(1)}T{hh:02d}:{m.group(3)}:00")
            offset = 4 if local.month < 11 or (local.month == 11 and local.day < 2) else 5
            report_ts = (local + timedelta(hours=offset)).replace(tzinfo=timezone.utc)
        for r in d.get("rows") or []:
            if r.get("status") in ("Out", "Doubtful", "Questionable") and r.get("player"):
                rows.append({"sport": "nba", "kind": f"injury_{r['status'].lower()}", "team": r.get("team"),
                             "detail": r.get("player"), "news_ts": report_ts or seen, "seen_ts": seen,
                             "game_start": None, "source": "NBA injury report"})
    df = pd.DataFrame(rows)
    if not df.empty:
        for c in ("news_ts", "seen_ts", "game_start"):
            df[c] = pd.to_datetime(df[c], utc=True, errors="coerce")
        df = df.sort_values("news_ts").drop_duplicates(subset=["sport", "kind", "team", "detail", "news_ts"])
    return df.reset_index(drop=True)


def _mid_at(path: pd.DataFrame, t: pd.Timestamp, after: bool) -> float | None:
    if path.empty:
        return None
    sel = path[path["t"] >= t] if after else path[path["t"] <= t]
    if sel.empty:
        return None
    return float(sel.iloc[0]["mid"] if after else sel.iloc[-1]["mid"])


def join_news_to_paths(events: pd.DataFrame, histories: list[dict], fair: pd.DataFrame, matches: pd.DataFrame,
                       pm_events: pd.DataFrame) -> pd.DataFrame:
    """One row per news event with a Polymarket WINNER contract for that team."""
    if events.empty or not histories:
        return pd.DataFrame()
    # index histories by (sport, event_id) -> list of WINNER docs
    docs: dict[tuple, list[dict]] = {}
    for d in histories:
        if d.get("market_class") == "WINNER":
            docs.setdefault((d["sport"], d["event_id"]), []).append(d)
    h2h = fair[fair["market"] == "h2h"] if not fair.empty else pd.DataFrame()
    out = []
    for _, ev in events.iterrows():
        if pd.isna(ev["news_ts"]) or not ev["team"]:
            continue
        # candidate Polymarket events: same sport, team name, start within 36h after the news
        cands = pm_events[(pm_events["sport"] == ev["sport"])]
        cands = cands[cands["team_names"].map(lambda ts: norm(ev["team"]) in {norm(x) for x in ts}
                                                     or nickname(ev["team"]) in {nickname(x) for x in ts})]
        cands = cands[(cands["start"] >= ev["news_ts"] - pd.Timedelta(hours=3)) &
                      (cands["start"] <= ev["news_ts"] + pd.Timedelta(hours=36))]
        if cands.empty:
            continue
        c = cands.sort_values("start").iloc[0]
        for d in docs.get((c["sport"], c["event_id"]), []):
            teams = d.get("teams") or []
            long_side = next((s for s in (d.get("sides") or []) if s.get("long")), None)
            long_team = next((t.get("name") for t in teams if long_side and t.get("id") == long_side.get("team_id")), None)
            path = pd.DataFrame(d.get("history") or [])
            if path.empty or "timestamp" not in path:
                continue
            path = path.dropna(subset=["mid"])
            path["t"] = pd.to_datetime(path["timestamp"], unit="s", utc=True)
            path = path.sort_values("t")
            t0 = ev["news_ts"]
            row = {"sport": ev["sport"], "kind": ev["kind"], "team": ev["team"], "detail": ev["detail"],
                   "news_ts": t0, "seen_ts": ev["seen_ts"], "source": ev["source"],
                   "pm_event_id": c["event_id"], "event_title": c["event_title"], "contract_team": long_team,
                   "contract_is_news_team": bool(long_team and (norm(long_team) == norm(ev["team"]) or nickname(long_team) == nickname(ev["team"]))),
                   "minutes_to_start": (c["start"] - t0).total_seconds() / 60 if pd.notna(c["start"]) else None,
                   "mid_before": _mid_at(path, t0 - pd.Timedelta(minutes=1), after=False),
                   "mid_plus5": _mid_at(path, t0 + pd.Timedelta(minutes=5), after=True),
                   "mid_plus15": _mid_at(path, t0 + pd.Timedelta(minutes=15), after=True),
                   "mid_plus30": _mid_at(path, t0 + pd.Timedelta(minutes=30), after=True),
                   "path_points": int(len(path))}
            for k in ("mid_plus5", "mid_plus15", "mid_plus30"):
                row[k.replace("mid_", "move_")] = (row[k] - row["mid_before"]) if (row[k] is not None and row["mid_before"] is not None) else None
            # Pinnacle fair for the contract team before and after the news
            if not h2h.empty and not matches.empty and long_team:
                m = matches[(matches["sport"] == c["sport"]) & (matches["pm_event_id"] == c["event_id"])]
                if not m.empty:
                    pf = h2h[(h2h["sport"] == c["sport"]) & (h2h["event_id"] == m.iloc[0]["pin_event_id"])]
                    sel = pf["outcome"].map(norm) == norm(long_team)
                    if not sel.any():
                        sel = pf["outcome"].map(nickname) == nickname(long_team)
                    pf = pf[sel].sort_values("ts")
                    before, after = pf[pf["ts"] <= t0], pf[pf["ts"] > t0]
                    row["pin_fair_before"] = float(before.iloc[-1]["fair_prob"]) if not before.empty else None
                    row["pin_ts_before"] = before.iloc[-1]["ts"] if not before.empty else None
                    row["pin_fair_after"] = float(after.iloc[0]["fair_prob"]) if not after.empty else None
                    row["pin_ts_after"] = after.iloc[0]["ts"] if not after.empty else None
                    if row.get("pin_fair_after") is not None:
                        # minutes until the Polymarket mid came within 1¢ of the new Pinnacle fair (pre-registered metric)
                        later = path[path["t"] >= t0]
                        hit = later[(later["mid"] - row["pin_fair_after"]).abs() <= 0.01]
                        row["minutes_to_within_1c"] = ((hit.iloc[0]["t"] - t0).total_seconds() / 60) if not hit.empty else None
            out.append(row)
    return pd.DataFrame(out)
