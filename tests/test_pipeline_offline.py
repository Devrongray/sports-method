"""Offline checks of the normalisers and test (c) using synthetic payloads."""
import io
from datetime import datetime, timedelta, timezone
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from method import polymarket_us as pm
from method.odds_api import normalize_odds, two_way_fair
from method.pinnacle_reliability import prepare, run


def test_event_market_normaliser():
    ev = {
        "id": "123", "slug": "lal-bos-2026-10-22", "title": "Lakers vs Celtics",
        "startTime": "2026-10-22T23:30:00Z", "live": False, "ended": False, "closed": False,
        "teams": [{"id": 1, "name": "Lakers", "abbreviation": "LAL"},
                  {"id": 2, "name": "Celtics", "abbreviation": "BOS"}],
        "markets": [
            {"id": "m1", "slug": "lal-bos-ml", "sportsMarketType": "SPORTS_MARKET_TYPE_MONEYLINE",
             "question": "Winner", "marketSides": [
                 {"id": "s1", "identifier": "LAL", "price": {"value": "0.44", "currency": "USD"}, "teamId": 1, "tradable": True},
                 {"id": "s2", "identifier": "BOS", "price": "0.57", "teamId": 2, "tradable": True}]},
            {"id": "m2", "slug": "lal-bos-total", "sportsMarketType": "SPORTS_MARKET_TYPE_TOTAL", "line": 224.5,
             "marketSides": []},
            {"id": "m3", "slug": "lal-bos-prop", "sportsMarketType": "SPORTS_MARKET_TYPE_PROP", "marketSides": []},
        ],
    }
    rows = list(pm.normalize_event_markets(ev, "nba", {"WINNER", "TOTAL"}))
    assert [r["market_class"] for r in rows] == ["WINNER", "TOTAL"]
    assert [r["market_type"] for r in rows] == ["MONEYLINE", "TOTAL"]       # legacy names still map
    assert all(r["is_main"] for r in rows)
    assert rows[0]["sides"][0]["price"] == 0.44 and rows[0]["sides"][1]["price"] == 0.57
    assert rows[1]["line"] == 224.5
    assert rows[0]["teams"][1]["abbr"] == "BOS"


def test_bbo_and_book_normalisers():
    md = {"marketSlug": "x", "bestBid": {"value": "0.55"}, "bestAsk": {"value": "0.57"},
          "bidShares": "1200", "askShares": "900", "bidDepth": 4, "askDepth": 3,
          "lastTradePx": {"value": "0.56"}, "state": "MARKET_STATE_OPEN",
          "lastPriceSample": {"longPx": {"value": "0.57"}, "shortPx": {"value": "0.45"}, "ts": "2026-10-22T20:00:00Z"}}
    b = pm.normalize_bbo(md)
    assert b["mid"] == pytest.approx(0.56) and b["spread"] == pytest.approx(0.02) and b["bid_shares"] == 1200
    book = pm.normalize_book({"marketSlug": "x", "bids": [{"px": {"value": "0.55"}, "qty": "100"}],
                              "offers": [{"px": {"value": "0.57"}, "qty": "50"}], "transactTime": "t"})
    assert book["bids"][0]["px"] == 0.55 and book["offers"][0]["qty"] == 50


def test_history_and_last_pregame_mid():
    start = datetime(2026, 10, 22, 23, 30, tzinfo=timezone.utc)
    pts = []
    for k in range(10):
        t = int((start - timedelta(minutes=10 - k)).timestamp())
        pts.append({"timestamp": t, "longPrice": 0.58, "shortPrice": 0.45 - 0.001 * k})
    rows = pm.normalize_history(pts)
    assert rows[0]["best_bid"] == 0.55 and rows[0]["best_ask"] == 0.58
    last = pm.last_pregame_mid(rows, start, cutoff_seconds=60)
    # the last point at or before start-60s is k=9 (one minute before start)
    assert last["timestamp"] == int((start - timedelta(minutes=1)).timestamp())


def test_odds_api_normaliser_and_devig():
    events = [{"id": "e1", "commence_time": "2026-10-22T23:30:00Z", "home_team": "A", "away_team": "B",
               "bookmakers": [{"key": "pinnacle", "last_update": "t", "markets": [
                   {"key": "h2h", "last_update": "t", "outcomes": [{"name": "A", "price": 1.80}, {"name": "B", "price": 2.15}]},
                   {"key": "totals", "last_update": "t", "outcomes": [{"name": "Over", "price": 1.95, "point": 224.5},
                                                                       {"name": "Under", "price": 1.95, "point": 224.5}]}]}]}]
    rows = list(normalize_odds(events, "basketball_nba", "now"))
    assert len(rows) == 4
    fair = two_way_fair(rows, "additive")
    h2h = {r["outcome"]: r["fair_prob"] for r in fair if r["market"] == "h2h"}
    assert abs(h2h["A"] + h2h["B"] - 1) < 1e-9 and h2h["A"] > 0.5
    tot = [r["fair_prob"] for r in fair if r["market"] == "totals"]
    assert tot == [0.5, 0.5]


def _fake_season(n=1500, seed=1, slope=1.0):
    """Synthetic 1X2 season. slope != 1 makes the odds miscalibrated:
    favourites too short (slope > 1 on the fair probabilities)."""
    rng = np.random.default_rng(seed)
    pH = rng.uniform(0.25, 0.65, n); pD = rng.uniform(0.18, 0.30, n); pA = 1 - pH - pD
    P = np.column_stack([pH, pD, pA]); P = P / P.sum(axis=1, keepdims=True)
    u = rng.uniform(size=n)
    cum = P.cumsum(axis=1)
    res = np.where(u < cum[:, 0], "H", np.where(u < cum[:, 1], "D", "A"))
    Q = P ** slope; Q = Q / Q.sum(axis=1, keepdims=True)   # what the book "believes"
    odds = 1 / (Q * 1.03)                                   # 3% multiplicative overround
    return pd.DataFrame({"PSCH": odds[:, 0], "PSCD": odds[:, 1], "PSCA": odds[:, 2], "FTR": res})


def test_prepare_drops_pricing_errors():
    df = _fake_season()
    df.loc[0, "PSCH"] = 50.0     # absurd price → overround collapses → dropped
    d = prepare(df, "PSC")
    assert len(d) == len(df) - 1
    assert {"oH", "oD", "oA", "FTR"} <= set(d.columns)


def test_test_c_passes_on_calibrated_data(tmp_path: Path):
    frames = [("2324", "E0", _fake_season(seed=1)), ("2324", "SP1", _fake_season(seed=2)),
              ("2425", "E0", _fake_season(seed=3)), ("2425", "SP1", _fake_season(seed=4))]
    verdict = run(frames, tmp_path, slope_band=(0.9, 1.1))
    assert verdict["pass"] is True
    assert verdict["best_devig_method"] in ("multiplicative", "additive", "power", "shin")
    assert set(verdict["seasons_slope_in_band"]) == {"2023/24", "2024/25"}
    assert (tmp_path / "summary.md").exists() and (tmp_path / "pooled_by_season.csv").exists()


def test_test_c_fails_on_miscalibrated_data(tmp_path: Path):
    # Book prices too extreme (slope 1.4): recalibration slope should fall well below 1
    frames = [("2324", "E0", _fake_season(seed=5, slope=1.4)), ("2324", "SP1", _fake_season(seed=6, slope=1.4))]
    verdict = run(frames, tmp_path, slope_band=(0.95, 1.05))
    assert verdict["pass"] is False


def test_collect_markets_with_stub_client():
    from method.snapshot import collect_markets, load_config
    cfg = load_config()
    now = datetime(2026, 10, 22, 20, 0, tzinfo=timezone.utc)

    class Stub:
        def league_events(self, slug):
            if slug != "nba":
                return []
            return [
                {"id": "1", "slug": "soon", "startTime": "2026-10-22T23:30:00Z",
                 "markets": [{"id": "a", "slug": "soon-ml", "sportsMarketType": "SPORTS_MARKET_TYPE_BASKETBALL_TEAM_FULL_GAME_WINNER", "marketSides": []},
                             {"id": "b", "slug": "soon-prop", "sportsMarketType": "SPORTS_MARKET_TYPE_PROP", "marketSides": []},
                             {"id": "t1", "slug": "soon-t-220", "sportsMarketType": "SPORTS_MARKET_TYPE_BASKETBALL_TEAM_FULL_GAME_TOTAL",
                              "line": 220.5, "marketSides": [{"identifier": "x-220pt5", "price": "0.62", "long": True}, {"identifier": "x-220pt5", "price": "0.63", "long": False}]},
                             {"id": "t2", "slug": "soon-t-224", "sportsMarketType": "SPORTS_MARKET_TYPE_BASKETBALL_TEAM_FULL_GAME_TOTAL",
                              "line": 224.5, "marketSides": [{"identifier": "x-224pt5", "price": "0.50", "long": True}, {"identifier": "x-224pt5", "price": "0.52", "long": False}]}]},
                {"id": "2", "slug": "far", "startTime": "2026-10-30T23:30:00Z",
                 "markets": [{"id": "c", "slug": "far-ml", "sportsMarketType": "SPORTS_MARKET_TYPE_BASKETBALL_TEAM_FULL_GAME_WINNER", "marketSides": []}]},
                {"id": "3", "slug": "done", "startTime": "2026-10-21T23:30:00Z", "ended": True,
                 "markets": [{"id": "d", "slug": "done-ml", "sportsMarketType": "SPORTS_MARKET_TYPE_BASKETBALL_TEAM_FULL_GAME_WINNER", "marketSides": []}]},
            ]

    from method.snapshot import collect_markets_full
    rows, everything = collect_markets_full(Stub(), cfg, now)
    # prop filtered, alt total dropped (main line only), far beyond horizon, ended dropped
    assert [r["market_slug"] for r in rows] == ["soon-ml", "soon-t-224"]
    assert rows[0]["sport"] == "nba" and abs(rows[0]["minutes_to_start"] - 210) < 1e-9
    assert [r["market_slug"] for r in everything] == ["soon-ml", "soon-prop", "soon-t-220", "soon-t-224"]
    assert [r["is_main"] for r in everything] == [True, True, False, True]
    assert collect_markets(Stub(), cfg, now) == rows


def test_discover_flags_wrong_slugs():
    from method.snapshot import discover, load_config
    cfg = load_config()
    now = datetime(2026, 10, 22, 20, 0, tzinfo=timezone.utc)

    class Stub:
        def leagues(self):
            return [{"slug": "nba", "name": "NBA"}, {"slug": "counter-strike", "name": "Counter-Strike 2"},
                    {"slug": "mlb", "name": "MLB"}]

        def league_events(self, slug):
            if slug == "nba":
                return [{"slug": "a", "startTime": "2026-10-22T23:30:00Z",
                         "markets": [{"sportsMarketType": "SPORTS_MARKET_TYPE_BASKETBALL_TEAM_FULL_GAME_WINNER"}]}]
            if slug == "cs2":
                raise RuntimeError("404")
            return []

    rep = discover(Stub(), cfg, now)
    by = {c["sport"]: c for c in rep["checks"]}
    assert by["nba"]["slug_listed"] and by["nba"]["upcoming_in_horizon"] == 1
    assert by["nba"]["market_types"] == {"BASKETBALL_TEAM_FULL_GAME_WINNER": 1}
    assert by["nba"]["market_classes"] == {"WINNER/FULL_GAME": 1} and by["nba"]["main_lines_in_horizon"] == 1
    assert not by["cs2"]["slug_listed"] and "404" in by["cs2"]["error"]
    assert "counter-strike" in by["cs2"]["candidates"]


@pytest.mark.parametrize("raw,cls,seg", [
    ("BASKETBALL_TEAM_FULL_GAME_WINNER", "WINNER", "FULL_GAME"),
    ("BASEBALL_TEAM_FULL_GAME_TOTAL", "TOTAL", "FULL_GAME"),
    ("HOCKEY_TEAM_FULL_GAME_SPREAD", "SPREAD", "FULL_GAME"),
    ("FOOTBALL_TEAM_POINTS_FULL_GAME_TOTAL", "TEAM_TOTAL", "FULL_GAME"),
    ("BASEBALL_TEAM_FIRST_FIVE_SPREAD", "SPREAD", "FIRST_FIVE"),
    ("BASEBALL_TEAM_INNING3_TOTAL", "TOTAL", "INNING3"),
    ("HOCKEY_TEAM_SECOND_PERIOD_TOTAL", "TOTAL", "SECOND_PERIOD"),
    ("FOOTBALL_GAME_FIRST_QUARTER_TOTAL", "TOTAL", "FIRST_QUARTER"),
    ("FOOTBALL_TEAM_FIRST_HALF_SPREAD", "SPREAD", "FIRST_HALF"),
    ("ESPORTS_MATCH_WINNER", "WINNER", "MATCH"),
    ("ESPORTS_MAP_ROUNDS_HANDICAP_2", "SPREAD", "MAP_2"),
    ("ESPORTS_MAP_TOTAL_ROUNDS_1", "TOTAL", "MAP_1"),
    ("ESPORTS_SERIES_MAP_HANDICAP", "SPREAD", "SERIES"),
    ("ESPORTS_SERIES_TOTAL_MAPS", "TOTAL", "SERIES"),
    ("MONEYLINE", "WINNER", "FULL_GAME"),
    ("SOMETHING_NEW", "OTHER", "UNKNOWN"),
])
def test_classify_real_type_names(raw, cls, seg):
    c, s, _ = pm.classify(raw)
    assert (c, s) == (cls, seg)


def test_nfl_half_team_total_disambiguation():
    # When a segment has both a GAME_ total and a TEAM_ total, the TEAM one is a team total.
    markets = [{"sportsMarketType": "FOOTBALL_GAME_FIRST_HALF_TOTAL", "line": 21.5, "marketSides": []},
               {"sportsMarketType": "FOOTBALL_TEAM_FIRST_HALF_TOTAL", "line": 10.5, "marketSides": [{"teamId": 7}]},
               {"sportsMarketType": "FOOTBALL_TEAM_FULL_GAME_TOTAL", "line": 44.5, "marketSides": []},
               {"sportsMarketType": "FOOTBALL_TEAM_POINTS_FULL_GAME_TOTAL", "line": 20.5, "marketSides": [{"teamId": 7}]}]
    parsed = pm.classify_event_markets(markets)
    assert [p[1] for p in parsed] == ["TOTAL", "TEAM_TOTAL", "TOTAL", "TEAM_TOTAL"]
    assert [p[2] for p in parsed] == ["FIRST_HALF", "FIRST_HALF", "FULL_GAME", "FULL_GAME"]


def test_main_line_picks_closest_to_even_per_team():
    # Sides are (bid, ask) of one contract, as in the live payload; the main line is the mid nearest 0.50.
    mk = lambda t, line, bid, ask, team=None: {
        "sportsMarketType": t, "line": line, "bestBidQuote": str(bid), "bestAskQuote": str(ask),
        "marketSides": [{"identifier": f"x-{line}", "price": str(bid), "long": True, "teamId": team},
                        {"identifier": f"x-{line}", "price": str(ask), "long": False, "teamId": team}]}
    markets = [mk("FOOTBALL_TEAM_FULL_GAME_TOTAL", 41.5, 0.70, 0.71), mk("FOOTBALL_TEAM_FULL_GAME_TOTAL", 44.5, 0.50, 0.52),
               mk("FOOTBALL_TEAM_FULL_GAME_TOTAL", 47.5, 0.30, 0.31),
               mk("FOOTBALL_TEAM_POINTS_FULL_GAME_TOTAL", 20.5, 0.50, 0.52, team=1),
               mk("FOOTBALL_TEAM_POINTS_FULL_GAME_TOTAL", 23.5, 0.40, 0.41, team=1),
               mk("FOOTBALL_TEAM_POINTS_FULL_GAME_TOTAL", 24.5, 0.49, 0.53, team=2)]
    parsed = pm.classify_event_markets(markets)
    assert pm.mark_main_lines(markets, parsed) == [False, True, False, True, False, True]
    assert pm.market_mid(markets[1]) == pytest.approx(0.51)


def test_main_line_on_real_nhl_ladder():
    # Montreal–Washington, 14 Oct 2026 pass: totals 2.5..9.5 with 1-cent spreads at every line.
    ladder = [(2.5, 0.98, 0.99), (3.5, 0.90, 0.91), (4.5, 0.83, 0.84), (5.5, 0.63, 0.64),
              (6.5, 0.51, 0.52), (7.5, 0.30, 0.31), (8.5, 0.22, 0.23), (9.5, 0.10, 0.11)]
    markets = [{"sportsMarketType": "HOCKEY_TEAM_FULL_GAME_TOTAL", "line": l,
                "marketSides": [{"identifier": f"t-{l}", "price": str(b), "long": True},
                                {"identifier": f"t-{l}", "price": str(a), "long": False}]} for l, b, a in ladder]
    parsed = pm.classify_event_markets(markets)
    mains = pm.mark_main_lines(markets, parsed)
    assert [l for (l, _, _), m in zip(ladder, mains) if m] == [6.5]
