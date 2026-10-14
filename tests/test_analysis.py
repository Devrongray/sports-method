"""End-to-end test of the daily analysis on a small synthetic data branch."""
import gzip
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pandas as pd
import pytest

from method.analysis import report
from method.analysis.match import norm, nickname, _teams_agree

T0 = datetime(2026, 10, 14, 21, 0, tzinfo=timezone.utc)      # recording time
START = datetime(2026, 10, 14, 23, 30, tzinfo=timezone.utc)   # game start


def _gz_ndjson(path: Path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(path, "wt") as f:
        for r in rows:
            f.write(json.dumps(r, default=str) + "\n")


def _gz_json(path: Path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(path, "wt") as f:
        json.dump(obj, f, default=str)


def _iso(t):
    return t.isoformat(timespec="seconds")


def build_data(root: Path):
    day = "2026-10-14"
    teams = [{"id": 1487, "name": "Montreal Canadiens", "abbr": "MTL"}, {"id": 1489, "name": "Washington Capitals", "abbr": "WSH"}]
    sides = [{"id": "s1", "identifier": "aec-nhl-mon-was", "price": 0.48, "long": True, "team_id": 1487},
             {"id": "s2", "identifier": "aec-nhl-mon-was", "price": 0.49, "long": False, "team_id": 1489}]
    market = {"league": "nhl", "event_id": "152366", "event_slug": "mtl-wsh", "event_title": "MTL Canadiens vs. WSH Capitals",
              "start": _iso(START), "teams": teams, "market_id": "m1", "market_slug": "aec-nhl-mon-was",
              "market_type": "HOCKEY_TEAM_FULL_GAME_WINNER", "market_class": "WINNER", "segment": "FULL_GAME",
              "is_main": True, "mid": 0.485, "line": None, "sides": sides, "sport": "nhl", "role": "windows",
              "minutes_to_start": 150.0, "ts": _iso(T0)}
    _gz_ndjson(root / "polymarket" / day / "markets_20261014T210000Z.ndjson.gz", [market])
    # Quotes: Polymarket mid for the Canadiens contract at three times
    bbo = []
    for k, mid in enumerate([0.485, 0.455, 0.445]):
        t = T0 + timedelta(minutes=10 * k)
        bbo.append({"ts": _iso(t), "sport": "nhl", "event_id": "152366", "start": _iso(START),
                    "market_type": "HOCKEY_TEAM_FULL_GAME_WINNER", "market_class": "WINNER", "segment": "FULL_GAME",
                    "line": None, "minutes_to_start": 150 - 10 * k, "market_slug": "aec-nhl-mon-was",
                    "best_bid": mid - 0.005, "best_ask": mid + 0.005, "mid": mid, "spread": 0.01,
                    "bid_shares": 30000, "ask_shares": 31000, "state": "MARKET_STATE_OPEN"})
    _gz_ndjson(root / "polymarket" / day / "bbo_20261014T210000Z.ndjson.gz", bbo)
    # Pinnacle: Capitals 1.72 / Canadiens 2.30 at T0 (fair MTL ≈ 0.43), then MTL drifts to 2.45 at T0+10
    pin = []
    for k, (pw, pm_) in enumerate([(1.72, 2.30), (1.68, 2.45)]):
        t = T0 + timedelta(minutes=10 * k)
        for outcome, price in (("Washington Capitals", pw), ("Montreal Canadiens", pm_)):
            pin.append({"ts": _iso(t), "sport_key": "icehockey_nhl", "event_id": "p1", "commence_time": _iso(START),
                        "home": "Washington Capitals", "away": "Montreal Canadiens", "bookmaker": "pinnacle",
                        "market": "h2h", "outcome": outcome, "price": price, "point": None, "sport": "nhl"})
    _gz_ndjson(root / "pinnacle" / day / "odds_20261014T210000Z.ndjson.gz", pin)
    _gz_json(root / "pinnacle" / day / "quota_20261014T210000Z.json.gz",
             {"ts": _iso(T0), "pinnacle_rows": 4, "sports": ["nhl"], "quota": {"remaining": 490, "used": 10, "last": 2}})
    # History: minute path from T0-60 to START, settlement 1 (Canadiens won)
    hist = []
    for m in range(-60, 150):
        t = T0 + timedelta(minutes=m)
        mid = 0.485 if m < 5 else 0.445      # drops 5 minutes after the goalie news at T0
        hist.append({"timestamp": int(t.timestamp()), "long_price": mid + 0.005, "short_price": 1 - (mid - 0.005),
                     "best_bid": mid - 0.005, "best_ask": mid + 0.005, "mid": mid, "spread": 0.01})
    _gz_json(root / "polymarket_history" / day / "aec-nhl-mon-was.json.gz",
             {"ts": _iso(START + timedelta(hours=5)), "sport": "nhl", "league": "nhl", "event_id": "152366",
              "event_slug": "mtl-wsh", "event_title": "MTL Canadiens vs. WSH Capitals", "start": _iso(START), "teams": teams,
              "market_slug": "aec-nhl-mon-was", "market_type": "HOCKEY_TEAM_FULL_GAME_WINNER", "market_class": "WINNER",
              "segment": "FULL_GAME", "line": None, "sides": sides, "fee_coefficient": 0.0695,
              "last_pregame": hist[-2], "settlement": 1.0, "n_points": len(hist), "history": hist})
    # News: Canadiens goalie confirmed at T0
    _gz_json(root / "news" / day / "nhl_goalies_20261014T210500Z.json.gz",
             {"ts": _iso(T0 + timedelta(minutes=5)), "games": [{
                 "date": day, "time": "19:30", "dateGmt": _iso(START), "pointSpread": 1.5,
                 "homeTeamName": "Washington Capitals", "homeGoalieName": "Charlie Lindgren", "homeNewsStrengthName": "Confirmed",
                 "homeNewsCreatedAt": _iso(T0 - timedelta(hours=3)), "homeNewsSourceName": "Tom Gulitti",
                 "awayTeamName": "Montreal Canadiens", "awayGoalieName": "Jakub Dobes", "awayNewsStrengthName": "Confirmed",
                 "awayNewsCreatedAt": _iso(T0), "awayNewsSourceName": "Marco D'Amico"}]})


def test_matching_helpers():
    assert norm("LA Dodgers") == "los angeles dodgers" and nickname("Montreal Canadiens") == "canadiens"
    assert _teams_agree(["Montreal Canadiens", "Washington Capitals"], ["Washington Capitals", "Montreal Canadiens"]) == "full"
    assert _teams_agree(["MTL Canadiens", "WSH Capitals"], ["Washington Capitals", "Montreal Canadiens"]) == "nick"
    assert _teams_agree(["Boston Bruins", "Washington Capitals"], ["Washington Capitals", "Montreal Canadiens"]) is None


def test_daily_report_end_to_end(tmp_path: Path):
    data, out = tmp_path / "data", tmp_path / "out"
    build_data(data)
    stats = report.run(data, out, today="2026-10-15")
    assert stats["matches"] == 1 and stats["compare_rows"] == 2 and stats["settled"] == 1
    cmp = pd.read_csv(out / "2026-10-15" / "compare.csv")
    # Canadiens contract vs Canadiens fair: additive de-vig of (1.72, 2.30): implied 0.581+0.435=1.016 → MTL fair ≈ 0.427
    assert cmp.iloc[0]["team"] == "Montreal Canadiens"
    assert cmp.iloc[0]["fair"] == pytest.approx(0.4268, abs=0.001)
    assert cmp.iloc[0]["mid_minus_fair"] == pytest.approx(0.485 - 0.4268, abs=0.001)
    assert cmp.iloc[1]["pm_mid"] == pytest.approx(0.455)           # nearest quote 10 min later
    settled = pd.read_csv(out / "2026-10-15" / "settled.csv")
    assert settled.iloc[0]["y"] == 1.0 and settled.iloc[0]["pin_close_fair"] == pytest.approx(0.4065, abs=0.001)
    ev = pd.read_csv(out / "2026-10-15" / "news_events.csv")
    assert set(ev["kind"]) == {"goalie_confirmed"} and len(ev) == 2
    j = pd.read_csv(out / "2026-10-15" / "news_joined.csv")
    canadiens = j[j["team"] == "Montreal Canadiens"].iloc[0]
    assert canadiens["contract_is_news_team"] == True
    assert canadiens["mid_before"] == pytest.approx(0.485) and canadiens["mid_plus15"] == pytest.approx(0.445)
    assert canadiens["move_plus15"] == pytest.approx(-0.04)
    assert canadiens["pin_fair_before"] == pytest.approx(0.4268, abs=0.001) and canadiens["pin_fair_after"] == pytest.approx(0.4065, abs=0.001)
    # mid reaches within 1c of the new fair? 0.445 vs 0.4065: no → NaN
    assert pd.isna(canadiens["minutes_to_within_1c"])
    md = (out / "latest.md").read_text()
    assert "Polymarket mid vs Pinnacle fair" in md and "Montreal Canadiens" in md and "goalie_confirmed" in md
