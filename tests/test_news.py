"""Offline tests for the news recorders (parsers and change detection)."""
from pathlib import Path

import pytest

from method.news import mlb, nba
from method.news.common import robots_allows


def _sched(lineup_home=None, prob_home="A. Ace"):
    g = {"gamePk": 777, "gameDate": "2026-10-15T00:00:00Z",
         "status": {"detailedState": "Pre-Game", "abstractGameState": "Preview"},
         "teams": {"home": {"team": {"id": 119, "name": "Los Angeles Dodgers"}, "probablePitcher": {"fullName": prob_home}},
                   "away": {"team": {"id": 158, "name": "Milwaukee Brewers"}, "probablePitcher": {"fullName": "B. Bat"}}}}
    if lineup_home is not None:
        g["lineups"] = {"homePlayers": [{"id": i, "fullName": n, "primaryPosition": {"abbreviation": "SS"}, "battingOrder": str((k + 1) * 100)}
                                        for k, (i, n) in enumerate(lineup_home)], "awayPlayers": []}
    return {"dates": [{"date": "2026-10-14", "games": [g]}]}


def test_mlb_canonical_and_diff():
    a = mlb.canonical(_sched())
    b = mlb.canonical(_sched(lineup_home=[(1, "Shohei Ohtani"), (2, "Mookie Betts")]))
    c = mlb.canonical(_sched(lineup_home=[(1, "Shohei Ohtani"), (2, "Mookie Betts")], prob_home="C. Closer"))
    assert a["777"]["lineup_home"] == [] and a["777"]["probable_home"] == "A. Ace"
    d1 = mlb.diff(a, b)
    assert [x["field"] for x in d1] == ["lineup_home"] and d1[0]["after"][0]["name"] == "Shohei Ohtani"
    d2 = mlb.diff(b, c)
    assert [x["field"] for x in d2] == ["probable_home"] and d2[0]["after"] == "C. Closer"
    assert mlb.diff({}, a)[0]["after"] == "new game"


def test_mlb_recorder_writes_only_on_change(tmp_path: Path, monkeypatch=None):
    rec = mlb.MLBLineups(tmp_path)
    states = iter([_sched(), _sched(), _sched(lineup_home=[(1, "Shohei Ohtani")])])
    rec.sess = type("S", (), {"get": lambda self, *a, **k: type("R", (), {"raise_for_status": lambda s: None,
                                                                           "json": lambda s: next(states)})()})()
    from datetime import datetime, timezone
    now = datetime(2026, 10, 14, 20, 0, tzinfo=timezone.utc)
    s1 = rec.poll(now)            # first poll: writes (two dates fetched -> both from the same iterator)
    assert s1["changed"] is True
    files = list((tmp_path / "news" / "2026-10-14").glob("mlb_lineups_*.json.gz"))
    assert len(files) == 1


NBA_TEXT = """Injury Report: 10/20/26 05:30 PM
Game Date Game Time Matchup Team Player Name Current Status Reason
10/20/2026 07:30 (ET) OKC@HOU Oklahoma City Thunder Holmgren, Chet Out Injury/Illness - Left Ankle; Sprain
Williams, Jalen Questionable Injury/Illness - Right Wrist; Soreness
Houston Rockets NOT YET SUBMITTED
10:00 (ET) GSW@LAL Golden State Warriors Curry, Stephen Available Injury/Illness - Left Knee; Management
Los Angeles Lakers James, LeBron Probable Rest
"""


def test_nba_parse_rows_carries_context_forward():
    rows = nba.parse_rows(NBA_TEXT)
    assert rows[0] == {"game_date": "10/20/2026", "game_time": "07:30 (ET)", "matchup": "OKC@HOU",
                       "team": "Oklahoma City Thunder", "player": "Holmgren, Chet", "status": "Out",
                       "reason": "Injury/Illness - Left Ankle; Sprain"}
    assert rows[1]["player"] == "Williams, Jalen" and rows[1]["status"] == "Questionable" and rows[1]["team"] == "Oklahoma City Thunder"
    assert rows[2]["status"] == "NOT YET SUBMITTED" and rows[2]["team"] == "Houston Rockets"
    assert rows[3]["matchup"] == "GSW@LAL" and rows[3]["game_time"] == "10:00 (ET)" and rows[3]["team"] == "Golden State Warriors"
    assert rows[4]["team"] == "Los Angeles Lakers" and rows[4]["status"] == "Probable" and rows[4]["reason"] == "Rest"


def test_nba_season_slug_and_pdf_regex():
    from datetime import datetime
    assert nba.season_slug(datetime(2026, 10, 14)) == "2026-27"
    assert nba.season_slug(datetime(2027, 3, 1)) == "2026-27"
    html = 'see <a href="https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-10-20_05_30PM.pdf">x</a>'
    assert nba.PDF_RE.findall(html) == ["https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-10-20_05_30PM.pdf"]


def test_robots_allows_parses_disallow(tmp_path):
    class R:
        def __init__(self, text, status=200):
            self.text, self.status_code = text, status

    class S:
        def __init__(self, text):
            self.text = text

        def get(self, url, timeout=10):
            return R(self.text)

    assert robots_allows(S("User-agent: *\nDisallow: /starting-goalies/\n"), "https://x", "/starting-goalies/") is False
    assert robots_allows(S("User-agent: *\nDisallow: /admin/\n"), "https://x", "/starting-goalies/") is True
    assert robots_allows(S("User-agent: *\nDisallow: /\nAllow: /starting-goalies/\n"), "https://x", "/starting-goalies/") is True
    assert robots_allows(S("User-agent: Googlebot\nDisallow: /\n"), "https://x", "/starting-goalies/") is True


def test_dailyfaceoff_parser_reads_embedded_json():
    from method.news.nhl import parse_dailyfaceoff
    page = ('<html><script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"data":[{"date":"2026-10-14",'
            '"time":"19:30","dateGmt":"2026-10-14T23:30:00.000Z","pointSpread":1.5,"homeTeamId":30,"homeTeamName":"Washington Capitals",'
            '"homeGoalieId":2615,"homeGoalieName":"Charlie Lindgren","homeNewsStrengthId":2,"homeNewsStrengthName":"Confirmed",'
            '"homeNewsDetails":"Lindgren will start.","homeNewsSourceName":"Tom Gulitti","homeNewsSourceUrl":"https://x.com/x",'
            '"homeNewsCreatedAt":"2026-10-14T21:01:39.432Z","awayTeamId":16,"awayTeamName":"Montreal Canadiens","awayGoalieId":31895,'
            '"awayGoalieName":"Jakub Dobes","awayNewsStrengthName":"Likely","awayNewsCreatedAt":"2026-10-13T14:08:54.208Z"}]}}}</script></html>')
    games = parse_dailyfaceoff(page)
    assert len(games) == 1
    g = games[0]
    assert g["homeGoalieName"] == "Charlie Lindgren" and g["homeNewsStrengthName"] == "Confirmed"
    assert g["homeNewsCreatedAt"] == "2026-10-14T21:01:39.432Z" and g["awayNewsStrengthName"] == "Likely"
    assert g["dateGmt"] == "2026-10-14T23:30:00.000Z"
    assert parse_dailyfaceoff("<html>no data</html>") == []
