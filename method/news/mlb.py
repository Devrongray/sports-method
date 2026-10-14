"""MLB official lineups and probable pitchers via the MLB StatsAPI.

    GET https://statsapi.mlb.com/api/v1/schedule?sportId=1&date=YYYY-MM-DD
        &hydrate=probablePitcher,lineups,team

The schedule carries, per game, the probable pitchers and (once posted,
usually 2–4 hours before first pitch) the batting orders. A record is written
whenever the canonical state of any game changes.
"""
from __future__ import annotations

from datetime import datetime, timedelta
from pathlib import Path

from .common import digest, session, stamp, utcnow, write_gz_json

BASE = "https://statsapi.mlb.com/api/v1/schedule"


def fetch_schedule(sess, date: str, timeout: float = 20) -> dict:
    r = sess.get(BASE, params={"sportId": 1, "date": date, "hydrate": "probablePitcher,lineups,team"},
                 timeout=timeout)
    r.raise_for_status()
    return r.json()


def _players(block) -> list[dict]:
    out = []
    for p in block or []:
        out.append({"id": p.get("id"), "name": p.get("fullName"),
                    "pos": (p.get("primaryPosition") or {}).get("abbreviation"),
                    "order": p.get("battingOrder")})
    return out


def canonical(schedule: dict) -> dict[str, dict]:
    """gamePk -> state that matters for pricing: status, probables, lineups."""
    games = {}
    for day in schedule.get("dates") or []:
        for g in day.get("games") or []:
            teams = g.get("teams") or {}
            home, away = teams.get("home") or {}, teams.get("away") or {}
            lu = g.get("lineups") or {}
            games[str(g.get("gamePk"))] = {
                "gamePk": g.get("gamePk"),
                "gameDate": g.get("gameDate"),
                "status": (g.get("status") or {}).get("detailedState"),
                "abstract": (g.get("status") or {}).get("abstractGameState"),
                "home": (home.get("team") or {}).get("name"),
                "away": (away.get("team") or {}).get("name"),
                "home_id": (home.get("team") or {}).get("id"),
                "away_id": (away.get("team") or {}).get("id"),
                "probable_home": (home.get("probablePitcher") or {}).get("fullName"),
                "probable_away": (away.get("probablePitcher") or {}).get("fullName"),
                "lineup_home": _players(lu.get("homePlayers")),
                "lineup_away": _players(lu.get("awayPlayers")),
            }
    return games


def diff(prev: dict[str, dict], cur: dict[str, dict]) -> list[dict]:
    """Field-level changes between two canonical states."""
    changes = []
    for pk, now in cur.items():
        before = prev.get(pk)
        if before is None:
            changes.append({"gamePk": pk, "field": "*", "before": None, "after": "new game"})
            continue
        for k in ("status", "probable_home", "probable_away", "lineup_home", "lineup_away"):
            if before.get(k) != now.get(k):
                changes.append({"gamePk": pk, "field": k, "before": before.get(k), "after": now.get(k)})
    return changes


class MLBLineups:
    def __init__(self, out: Path):
        self.out = out
        self.sess = session()
        self.prev: dict[str, dict] = {}
        self.prev_digest = None

    def poll(self, now: datetime | None = None) -> dict:
        now = now or utcnow()
        state: dict[str, dict] = {}
        for d in (now.date(), (now + timedelta(days=1)).date()):
            try:
                state.update(canonical(fetch_schedule(self.sess, d.isoformat())))
            except Exception as e:
                print(f"[warn] mlb schedule {d}: {e}")
        dg = digest(state)
        changed = dg != self.prev_digest
        summary = {"ts": now.isoformat(timespec="seconds"), "games": len(state), "changed": changed}
        if changed:
            changes = diff(self.prev, state) if self.prev else []
            doc = {"ts": summary["ts"], "first_poll_of_run": not self.prev, "changes": changes, "state": state}
            write_gz_json(self.out / "news" / now.strftime("%Y-%m-%d") / f"mlb_lineups_{stamp(now)}.json.gz", doc)
            summary["n_changes"] = len(changes)
            self.prev, self.prev_digest = state, dg
        return summary
