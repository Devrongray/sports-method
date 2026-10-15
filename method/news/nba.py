"""NBA official injury reports.

The league publishes a PDF several times a day on game days at
https://official.nba.com/nba-injury-report-<season>/ with links like
https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-10-20_05_30PM.pdf
Each new PDF is downloaded once per run, its text extracted (pypdf), parsed
into rows (game date, game time, matchup, team, player, status, reason), and
stored with the raw text so the parser can be corrected later from real
reports. The report's own time is in the file name; `ts` is when we saw it.
"""
from __future__ import annotations

import io
import re
from datetime import datetime
from pathlib import Path

from .common import session, stamp, utcnow, write_gz_json

INDEX = "https://official.nba.com/nba-injury-report-{season}/"
PDF_RE = re.compile(r"https?://[^\s\"'>]+Injury-Report[^\s\"'>]*\.pdf", re.I)
STATUS = ("Out", "Doubtful", "Questionable", "Probable", "Available")
# "Last, First" immediately followed by the status word; the last name is
# whatever remains after the team name is stripped from the text before it.
NAME_STATUS_RE = re.compile(r"^(?P<before>.*?), (?P<first>[A-Z][\w'\.\-]*(?: [A-Z][\w'\.\-]*)?) (?P<status>Out|Doubtful|Questionable|Probable|Available)\b(?P<reason>.*)$")
TEAMS = ["Atlanta Hawks", "Boston Celtics", "Brooklyn Nets", "Charlotte Hornets", "Chicago Bulls",
         "Cleveland Cavaliers", "Dallas Mavericks", "Denver Nuggets", "Detroit Pistons", "Golden State Warriors",
         "Houston Rockets", "Indiana Pacers", "LA Clippers", "Los Angeles Clippers", "Los Angeles Lakers",
         "Memphis Grizzlies", "Miami Heat", "Milwaukee Bucks", "Minnesota Timberwolves", "New Orleans Pelicans",
         "New York Knicks", "Oklahoma City Thunder", "Orlando Magic", "Philadelphia 76ers", "Phoenix Suns",
         "Portland Trail Blazers", "Sacramento Kings", "San Antonio Spurs", "Toronto Raptors", "Utah Jazz",
         "Washington Wizards"]
MATCHUP_RE = re.compile(r"\b([A-Z]{3})@([A-Z]{3})\b")
TIME_RE = re.compile(r"\b(\d{1,2}:\d{2} ?\(ET\))")
DATE_RE = re.compile(r"\b(\d{2}/\d{2}/\d{4})\b")


def season_slug(now: datetime) -> str:
    y = now.year if now.month >= 7 else now.year - 1
    return f"{y}-{str(y + 1)[-2:]}"


def pdf_text(data: bytes) -> str:
    try:
        from pypdf import PdfReader
    except ImportError:  # pragma: no cover
        return ""
    reader = PdfReader(io.BytesIO(data))
    return "\n".join((p.extract_text() or "") for p in reader.pages)


def parse_rows(text: str) -> list[dict]:
    """Heuristic line parser. Values carry forward (date, time, matchup, team)
    the way the PDF leaves them blank on continuation lines."""
    rows = []
    ctx = {"game_date": None, "game_time": None, "matchup": None, "team": None}
    for raw in text.splitlines():
        line = " ".join(raw.split())
        if not line or line.startswith(("Injury Report", "Page", "Game Date")):
            continue
        m = DATE_RE.search(line)
        if m:
            ctx["game_date"] = m.group(1)
        m = TIME_RE.search(line)
        if m:
            ctx["game_time"] = m.group(1)
        m = MATCHUP_RE.search(line)
        if m:
            ctx["matchup"] = m.group(0)
        core = MATCHUP_RE.sub("", TIME_RE.sub("", DATE_RE.sub("", line))).strip()
        m = NAME_STATUS_RE.match(core)
        if m:
            before = m.group("before").strip()
            for t in TEAMS:
                if before.startswith(t + " "):
                    ctx["team"] = t
                    before = before[len(t):].strip()
                    break
            rows.append({**ctx, "player": f"{before}, {m.group('first')}", "status": m.group("status"),
                         "reason": m.group("reason").strip() or None})
        elif "NOT YET SUBMITTED" in core.upper():
            team_part = core.upper().split("NOT YET SUBMITTED")[0].strip()
            for t in TEAMS:
                if team_part.startswith(t.upper()):
                    ctx["team"] = t
                    break
            rows.append({**ctx, "player": None, "status": "NOT YET SUBMITTED", "reason": None})
    return rows


class NBAInjuryReports:
    def __init__(self, out: Path):
        self.out = out
        self.sess = session()
        self.seen: set[str] = set()

    def list_pdfs(self, now: datetime) -> list[str]:
        url = INDEX.format(season=season_slug(now))
        status, text, err = None, "", None
        try:
            r = self.sess.get(url, timeout=20)
            status, text = r.status_code, r.text
            r.raise_for_status()
        except Exception as e:
            err = str(e)[:200]
            print(f"[warn] nba index: {e}")
        urls = sorted(set(PDF_RE.findall(text)))
        if not getattr(self, "_index_logged", False):
            # diagnostic once per run: what the index page looked like
            write_gz_json(self.out / "news" / now.strftime("%Y-%m-%d") / f"nba_index_{stamp(now)}.json.gz",
                          {"ts": now.isoformat(timespec="seconds"), "url": url, "status": status, "error": err,
                           "n_pdf_links": len(urls), "sample_links": urls[:5], "page_bytes": len(text),
                           "page_head": text[:3000]})
            self._index_logged = True
        return urls

    def poll(self, now: datetime | None = None) -> dict:
        now = now or utcnow()
        urls = self.list_pdfs(now)
        new = [u for u in urls if u not in self.seen]
        written = 0
        for u in new:
            try:
                r = self.sess.get(u, timeout=30)
                r.raise_for_status()
                data = r.content
            except Exception as e:
                print(f"[warn] nba pdf {u}: {e}")
                continue
            text = pdf_text(data)
            doc = {"ts": now.isoformat(timespec="seconds"), "url": u, "bytes": len(data),
                   "rows": parse_rows(text), "text": text}
            name = u.rsplit("/", 1)[-1].replace(".pdf", "")
            write_gz_json(self.out / "news" / now.strftime("%Y-%m-%d") / f"nba_injury_{name}_{stamp(now)}.json.gz", doc)
            self.seen.add(u)
            written += 1
        return {"ts": now.isoformat(timespec="seconds"), "listed": len(urls), "new": written}
