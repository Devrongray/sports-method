"""NHL starting goalies: DailyFaceoff's page, recorded raw.

There is no official pre-game source for confirmed starters. DailyFaceoff
(https://www.dailyfaceoff.com/starting-goalies/) is what the market reads.
The page is fetched only if its robots.txt allows the path, at most every
few minutes, and stored gzipped whenever its content hash changes; the
parser is written later from stored pages. Alongside, the NHL API schedule
(official) is recorded for game states and start times.
"""
from __future__ import annotations

from datetime import datetime
from pathlib import Path

from .common import digest, robots_allows, session, stamp, utcnow, write_gz_bytes, write_gz_json

DFO_BASE = "https://www.dailyfaceoff.com"
DFO_PATH = "/starting-goalies/"
NHL_SCHEDULE = "https://api-web.nhle.com/v1/schedule/now"


class NHLGoalies:
    def __init__(self, out: Path):
        self.out = out
        self.sess = session()
        self.allowed: bool | None = None
        self.prev_page = None
        self.prev_sched = None

    def poll(self, now: datetime | None = None) -> dict:
        now = now or utcnow()
        day = now.strftime("%Y-%m-%d")
        summary = {"ts": now.isoformat(timespec="seconds")}
        if self.allowed is None:
            self.allowed = robots_allows(self.sess, DFO_BASE, DFO_PATH)
            summary["dailyfaceoff_allowed"] = self.allowed
        if self.allowed:
            try:
                r = self.sess.get(DFO_BASE + DFO_PATH, timeout=20)
                r.raise_for_status()
                dg = digest(r.content)
                if dg != self.prev_page:
                    write_gz_bytes(self.out / "news" / day / f"nhl_dailyfaceoff_{stamp(now)}.html.gz", r.content)
                    self.prev_page = dg
                    summary["dailyfaceoff"] = "changed"
                else:
                    summary["dailyfaceoff"] = "same"
            except Exception as e:
                print(f"[warn] dailyfaceoff: {e}")
        try:
            r = self.sess.get(NHL_SCHEDULE, timeout=20)
            r.raise_for_status()
            sched = r.json()
            games = []
            for wk in sched.get("gameWeek") or []:
                for g in wk.get("games") or []:
                    games.append({"id": g.get("id"), "date": wk.get("date"), "startTimeUTC": g.get("startTimeUTC"),
                                  "state": g.get("gameState"), "home": (g.get("homeTeam") or {}).get("abbrev"),
                                  "away": (g.get("awayTeam") or {}).get("abbrev")})
            dg = digest(games)
            if dg != self.prev_sched:
                write_gz_json(self.out / "news" / day / f"nhl_schedule_{stamp(now)}.json.gz",
                              {"ts": summary["ts"], "games": games})
                self.prev_sched = dg
                summary["nhl_schedule"] = "changed"
        except Exception as e:
            print(f"[warn] nhl schedule: {e}")
        return summary
