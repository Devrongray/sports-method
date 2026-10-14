"""NHL starting goalies: DailyFaceoff's page, recorded raw.

There is no official pre-game source for confirmed starters. DailyFaceoff
(https://www.dailyfaceoff.com/starting-goalies/) is what the market reads.
The page is fetched only if its robots.txt allows the path, at most every
few minutes, and parsed from its embedded JSON (goalie, confirmation strength, the time the
confirmation was posted, the source) and written whenever anything changes;
the raw page is kept once per run and whenever the parse fails. Alongside, the NHL API schedule
(official) is recorded for game states and start times.
"""
from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path

from .common import digest, robots_allows, session, stamp, utcnow, write_gz_bytes, write_gz_json

NEXT_DATA_RE = re.compile(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', re.S)
GOALIE_FIELDS = ("TeamId", "TeamName", "GoalieId", "GoalieName", "NewsStrengthId", "NewsStrengthName",
                 "NewsDetails", "NewsSourceName", "NewsSourceUrl", "NewsCreatedAt", "TeamMoneylinePointSpread")


def parse_dailyfaceoff(html: str) -> list[dict]:
    """Games from the page's embedded Next.js JSON (seen 14 Oct 2026):
    pageProps.data[] with home*/away* goalie fields, including
    <side>NewsStrengthName ("Confirmed", "Likely", ...) and <side>NewsCreatedAt,
    the time the confirmation was posted, which is the news timestamp."""
    m = NEXT_DATA_RE.search(html)
    if not m:
        return []
    data = json.loads(m.group(1))
    games = (((data.get("props") or {}).get("pageProps") or {}).get("data")) or []
    out = []
    for g in games:
        row = {"date": g.get("date"), "time": g.get("time"), "dateGmt": g.get("dateGmt"),
               "pointSpread": g.get("pointSpread")}
        for side in ("home", "away"):
            for f in GOALIE_FIELDS:
                row[f"{side}{f}"] = g.get(f"{side}{f}")
        out.append(row)
    return out

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
                games = parse_dailyfaceoff(r.text)
                if not games:
                    # structure changed: keep the raw page so the parser can be fixed
                    write_gz_bytes(self.out / "news" / day / f"nhl_dailyfaceoff_{stamp(now)}.html.gz", r.content)
                    summary["dailyfaceoff"] = "unparsed"
                else:
                    dg = digest(games)
                    if dg != self.prev_page:
                        write_gz_json(self.out / "news" / day / f"nhl_goalies_{stamp(now)}.json.gz",
                                      {"ts": summary["ts"], "games": games})
                        if self.prev_page is None:
                            write_gz_bytes(self.out / "news" / day / f"nhl_dailyfaceoff_{stamp(now)}.html.gz", r.content)
                        self.prev_page = dg
                        summary["dailyfaceoff"] = f"changed ({len(games)} games)"
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
