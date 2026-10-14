"""Pair Polymarket US events with Pinnacle (Odds API) events.

Polymarket teams carry full names and abbreviations; The Odds API uses full
names (e.g. "Los Angeles Dodgers"). Matching: same sport, start times within
a tolerance, and both teams' names agreeing after normalisation (full name,
or nickname = last word, as a fallback). Each pairing records how it was made
so weak matches can be reviewed.
"""
from __future__ import annotations

import re
from datetime import timedelta

import pandas as pd

_PUNCT = re.compile(r"[^a-z0-9 ]+")
ALIASES = {
    "la clippers": "los angeles clippers", "la lakers": "los angeles lakers", "la dodgers": "los angeles dodgers",
    "la angels": "los angeles angels", "la rams": "los angeles rams", "la chargers": "los angeles chargers",
    "la kings": "los angeles kings", "ny yankees": "new york yankees", "ny mets": "new york mets",
    "ny knicks": "new york knicks", "ny giants": "new york giants", "ny jets": "new york jets",
    "ny rangers": "new york rangers", "ny islanders": "new york islanders", "st louis": "st. louis",
    "utah hockey club": "utah mammoth", "washington football team": "washington commanders",
}


def norm(name: str | None) -> str:
    if not name:
        return ""
    s = _PUNCT.sub("", str(name).lower().replace("&", "and")).strip()
    s = re.sub(r"\s+", " ", s)
    return ALIASES.get(s, s)


def nickname(name: str | None) -> str:
    n = norm(name)
    return n.split(" ")[-1] if n else ""


def _teams_agree(a: list[str], b: list[str]) -> str | None:
    """'full' if both names match in full, 'nick' if by nickname, else None."""
    an, bn = {norm(x) for x in a if x}, {norm(x) for x in b if x}
    if len(an) == 2 and an == bn:
        return "full"
    ak, bk = {nickname(x) for x in a if x}, {nickname(x) for x in b if x}
    if len(ak) == 2 and ak == bk:
        return "nick"
    return None


def match_events(pm_events: pd.DataFrame, pin_events: pd.DataFrame, tolerance_minutes: int = 90) -> pd.DataFrame:
    """pm_events: one row per Polymarket event (sport, event_id, start, team_names).
    pin_events: one row per Odds API event (sport, event_id, commence_time, home, away).
    Returns rows: sport, pm_event_id, pin_event_id, how, minutes_apart."""
    out = []
    tol = timedelta(minutes=tolerance_minutes)
    pin_by_sport = {s: g for s, g in pin_events.groupby("sport")}
    for _, e in pm_events.iterrows():
        cands = pin_by_sport.get(e["sport"])
        if cands is None or pd.isna(e["start"]):
            continue
        near = cands[(cands["commence_time"] - e["start"]).abs() <= tol]
        best = None
        for _, c in near.iterrows():
            how = _teams_agree(list(e["team_names"]), [c["home"], c["away"]])
            if how is None:
                continue
            gap = abs((c["commence_time"] - e["start"]).total_seconds()) / 60
            rank = (0 if how == "full" else 1, gap)
            if best is None or rank < best[0]:
                best = (rank, c["event_id"], how, gap)
        if best:
            out.append({"sport": e["sport"], "pm_event_id": e["event_id"], "pin_event_id": best[1],
                        "how": best[2], "minutes_apart": round(best[3], 1),
                        "pm_teams": " / ".join(str(x) for x in e["team_names"])})
    return pd.DataFrame(out, columns=["sport", "pm_event_id", "pin_event_id", "how", "minutes_apart", "pm_teams"])


def pm_event_table(markets: pd.DataFrame) -> pd.DataFrame:
    if markets.empty:
        return pd.DataFrame(columns=["sport", "event_id", "start", "team_names", "event_title"])
    g = markets.sort_values("ts").groupby(["sport", "event_id"], as_index=False).last()
    return g[["sport", "event_id", "start", "team_names", "event_title"]]


def pin_event_table(pin: pd.DataFrame) -> pd.DataFrame:
    if pin.empty:
        return pd.DataFrame(columns=["sport", "event_id", "commence_time", "home", "away"])
    g = pin.sort_values("ts").groupby(["sport", "event_id"], as_index=False).last()
    return g[["sport", "event_id", "commence_time", "home", "away"]]
