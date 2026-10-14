from __future__ import annotations

import gzip
import json
from pathlib import Path
from typing import Iterator

import pandas as pd


def _ndjson(path: Path) -> Iterator[dict]:
    with gzip.open(path, "rt", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                yield json.loads(line)


def _json(path: Path) -> dict:
    with gzip.open(path, "rt", encoding="utf-8") as f:
        return json.load(f)


def _days(root: Path, since: str | None) -> list[Path]:
    if not root.exists():
        return []
    days = sorted(p for p in root.iterdir() if p.is_dir())
    if since:
        days = [d for d in days if d.name >= since]
    return days


def load_bbo(data: Path, since: str | None = None) -> pd.DataFrame:
    """Full-pass (bbo_) and window-pass (bbow_) quote rows, with `pass_scope`."""
    rows = []
    for day in _days(data / "polymarket", since):
        for f in sorted(day.glob("bbo*_*.ndjson.gz")):
            scope = "window" if f.name.startswith("bbow_") else "full"
            for r in _ndjson(f):
                r["pass_scope"] = scope
                rows.append(r)
    df = pd.DataFrame(rows)
    if not df.empty:
        df["ts"] = pd.to_datetime(df["ts"], utc=True)
        df["start"] = pd.to_datetime(df["start"], utc=True, errors="coerce")
    return df


def load_markets(data: Path, since: str | None = None) -> pd.DataFrame:
    """Main-line market rows (one per market per full pass), with team names and the
    team the long side pays for."""
    rows = []
    for day in _days(data / "polymarket", since):
        for f in sorted(day.glob("markets_*.ndjson.gz")):
            for r in _ndjson(f):
                teams = r.get("teams") or []
                long_side = next((s for s in (r.get("sides") or []) if s.get("long")), None)
                r["team_names"] = [t.get("name") for t in teams]
                r["team_abbrs"] = [t.get("abbr") for t in teams]
                r["long_team_id"] = long_side.get("team_id") if long_side else None
                r["long_team_name"] = next((t.get("name") for t in teams if long_side and t.get("id") == long_side.get("team_id")), None)
                r.pop("sides", None)
                r.pop("teams", None)
                rows.append(r)
    df = pd.DataFrame(rows)
    if not df.empty:
        df["ts"] = pd.to_datetime(df["ts"], utc=True)
        df["start"] = pd.to_datetime(df["start"], utc=True, errors="coerce")
    return df


def load_pinnacle(data: Path, since: str | None = None) -> pd.DataFrame:
    rows = []
    for day in _days(data / "pinnacle", since):
        for f in sorted(day.glob("odds_*.ndjson.gz")):
            rows.extend(_ndjson(f))
    df = pd.DataFrame(rows)
    if not df.empty:
        df["ts"] = pd.to_datetime(df["ts"], utc=True)
        df["commence_time"] = pd.to_datetime(df["commence_time"], utc=True, errors="coerce")
    return df


def load_histories(data: Path, since: str | None = None) -> list[dict]:
    docs = []
    for day in _days(data / "polymarket_history", since):
        for f in sorted(day.glob("*.json.gz")):
            docs.append(_json(f))
    return docs


def load_news(data: Path, since: str | None = None) -> dict[str, list[dict]]:
    out: dict[str, list[dict]] = {"mlb": [], "nba": [], "nhl": [], "nhl_schedule": []}
    for day in _days(data / "news", since):
        for f in sorted(day.glob("*.json.gz")):
            doc = _json(f)
            doc["_file"] = f.name
            if f.name.startswith("mlb_lineups_"):
                out["mlb"].append(doc)
            elif f.name.startswith("nba_injury_"):
                out["nba"].append(doc)
            elif f.name.startswith("nhl_goalies_"):
                out["nhl"].append(doc)
            elif f.name.startswith("nhl_schedule_"):
                out["nhl_schedule"].append(doc)
    return out


def load_quota(data: Path) -> pd.DataFrame:
    rows = []
    for day in _days(data / "pinnacle", None):
        for f in sorted(day.glob("quota_*.json.gz")):
            d = _json(f)
            rows.append({"ts": d.get("ts"), "rows": d.get("pinnacle_rows"), "sports": ",".join(d.get("sports") or []),
                         **{f"quota_{k}": v for k, v in (d.get("quota") or {}).items()}})
    return pd.DataFrame(rows)
