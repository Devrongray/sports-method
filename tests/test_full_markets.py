"""The league events feed embeds only the full-game winner per event since
2026-10-15 ~20:34 UTC; the recorder must fetch each event's full market list.
Offline checks with stub clients."""
from datetime import datetime, timezone

from method import polymarket_us as pm
from method.snapshot import collect_markets_full, discover, load_config

WIN = "SPORTS_MARKET_TYPE_HOCKEY_TEAM_FULL_GAME_WINNER"
TOT = "SPORTS_MARKET_TYPE_HOCKEY_TEAM_FULL_GAME_TOTAL"
P1T = "SPORTS_MARKET_TYPE_HOCKEY_TEAM_FIRST_PERIOD_TOTAL"


def _sides(a, b):
    return [{"identifier": "x", "price": str(a), "long": True}, {"identifier": "x", "price": str(b), "long": False}]


def _league_event(slug="nhl-pit-col-2026-10-16", start="2026-10-16T23:00:00Z", n=157):
    """What /v2/leagues/{slug}/events serves now: one nested market, a count of many."""
    return {"id": "1", "slug": slug, "startTime": start, "ended": False, "closed": False,
            "teams": [{"id": 1497, "name": "Penguins", "abbreviation": "PIT"}, {"id": 1502, "name": "Avalanche", "abbreviation": "COL"}],
            "markets": [{"id": "w", "slug": f"{slug}-ml", "sportsMarketType": WIN, "marketSides": _sides(0.34, 0.35)}],
            "marketCounts": {"numMarkets": n, "numSpreadsAndTotalsMarkets": 38}}


def _full_event(slug="nhl-pit-col-2026-10-16", start="2026-10-16T23:00:00Z"):
    """What /v1/events/slug/{slug} serves: the whole list (no marketCounts, no teams here on purpose)."""
    return {"id": "1", "slug": slug, "startTime": start, "title": "PIT Penguins vs COL Avalanche",
            "markets": [
                {"id": "w", "slug": f"{slug}-ml", "sportsMarketType": WIN, "marketSides": _sides(0.34, 0.35)},
                {"id": "t60", "slug": f"{slug}-6pt0", "sportsMarketType": TOT, "line": 6.0, "marketSides": _sides(0.44, 0.46)},
                {"id": "t65", "slug": f"{slug}-6pt5", "sportsMarketType": TOT, "line": 6.5, "marketSides": _sides(0.30, 0.33)},
                {"id": "p1", "slug": f"{slug}-p1-1pt5", "sportsMarketType": P1T, "line": 1.5, "marketSides": _sides(0.50, 0.53)},
            ]}


class Stub:
    """full: a document to return for every slug, or "per_slug" to build one for the slug asked."""

    def __init__(self, full=None, error=None):
        self.full = full
        self.error = error
        self.calls: list[str] = []
        self.events: list[dict] = []

    def league_events(self, slug):
        return [] if slug != "nhl" else self.events

    def event_full(self, event_slug):
        self.calls.append(event_slug)
        if self.error:
            raise self.error
        if self.full == "per_slug":
            start = next(e["startTime"] for e in self.events if e["slug"] == event_slug)
            return _full_event(slug=event_slug, start=start)
        return self.full


def test_truncation_detection_uses_the_feed_count_when_present():
    assert pm.markets_truncated(_league_event(n=157))
    assert not pm.markets_truncated({**_league_event(), "marketCounts": {"numMarkets": 1}})
    # no count: a single market is treated as truncated, several are not
    assert pm.markets_truncated({"markets": [{}]})
    assert not pm.markets_truncated({"markets": [{}, {}, {}]})
    assert pm.markets_truncated({"markets": [], "marketCounts": {"numMarkets": "oops"}})


def test_with_full_markets_merges_and_keeps_feed_only_fields():
    c = Stub(full=_full_event())
    ev = pm.with_full_markets(c, _league_event())
    assert c.calls == ["nhl-pit-col-2026-10-16"]
    assert [m["id"] for m in ev["markets"]] == ["w", "t60", "t65", "p1"]
    assert ev["teams"][0]["abbreviation"] == "PIT"          # kept from the league feed
    assert ev["marketCounts"]["numMarkets"] == 157            # kept from the league feed
    assert ev["title"] == "PIT Penguins vs COL Avalanche"     # added from the full document
    rows = list(pm.normalize_event_markets(ev, "nhl", {"WINNER", "TOTAL"}, main_only=True))
    assert sorted(r["market_slug"] for r in rows) == sorted([
        "nhl-pit-col-2026-10-16-ml", "nhl-pit-col-2026-10-16-6pt0", "nhl-pit-col-2026-10-16-p1-1pt5"])


def test_with_full_markets_is_a_no_op_when_not_needed_or_not_possible():
    whole = {**_league_event(), "marketCounts": {"numMarkets": 1}}
    c = Stub(full=_full_event())
    assert pm.with_full_markets(c, whole) is whole and c.calls == []
    no_slug = {k: v for k, v in _league_event().items() if k != "slug"}
    assert pm.with_full_markets(c, no_slug) is no_slug and c.calls == []
    # failure keeps the pass alive and returns the event as served
    for bad in (Stub(error=RuntimeError("503")), Stub(full=None), Stub(full={"markets": []})):
        ev = _league_event()
        assert pm.with_full_markets(bad, ev) is ev
    # a client without event_full (older stubs) is left alone
    class NoFetch:
        pass
    ev = _league_event()
    assert pm.with_full_markets(NoFetch(), ev) is ev


def test_collect_markets_full_expands_inside_the_horizon_and_respects_the_window_limit():
    cfg = load_config()
    now = datetime(2026, 10, 16, 20, 0, tzinfo=timezone.utc)
    c = Stub(full="per_slug")
    c.events = [_league_event(),                                                          # 180 min out
                _league_event(slug="nhl-bos-ana-2026-10-17", start="2026-10-17T02:00:00Z"),  # 360 min out
                _league_event(slug="nhl-far-2026-10-19", start="2026-10-19T02:00:00Z")]      # beyond horizon
    kept, everything = collect_markets_full(c, cfg, now)
    assert c.calls == ["nhl-pit-col-2026-10-16", "nhl-bos-ana-2026-10-17"]
    classes = {(r["market_slug"], r["market_class"], r["segment"]) for r in kept if r["market_slug"].startswith("nhl-pit")}
    assert ("nhl-pit-col-2026-10-16-6pt0", "TOTAL", "FULL_GAME") in classes
    assert ("nhl-pit-col-2026-10-16-p1-1pt5", "TOTAL", "FIRST_PERIOD") in classes
    assert len([r for r in everything if r["market_slug"].startswith("nhl-pit")]) == 4
    assert len([r for r in everything if r["market_slug"].startswith("nhl-bos")]) == 4
    assert not any(r["market_slug"].startswith("nhl-far") for r in everything)

    # window pass: only events inside the window are expanded
    c2 = Stub(full="per_slug")
    c2.events = c.events
    kept2, _ = collect_markets_full(c2, cfg, now, expand_within_minutes=cfg["cadence"]["pre_start_window_minutes"])
    assert c2.calls == []                      # nothing inside 90 minutes
    now2 = datetime(2026, 10, 16, 22, 0, tzinfo=timezone.utc)   # PIT@COL now 60 min out
    c3 = Stub(full="per_slug")
    c3.events = c.events
    collect_markets_full(c3, cfg, now2, expand_within_minutes=90)
    assert c3.calls == ["nhl-pit-col-2026-10-16"]


def test_discover_counts_the_full_market_list():
    cfg = load_config()
    now = datetime(2026, 10, 16, 20, 0, tzinfo=timezone.utc)

    class DiscoverStub(Stub):
        def leagues(self):
            return [{"slug": s["polymarket_league"], "name": s["name"]} for s in cfg["sports"]]

    c = DiscoverStub(full=_full_event())
    c.events = [_league_event()]
    rep = discover(c, cfg, now)
    nhl = {x["sport"]: x for x in rep["checks"]}["nhl"]
    assert nhl["upcoming_in_horizon"] == 1
    assert nhl["market_types"] == {"HOCKEY_TEAM_FULL_GAME_WINNER": 1, "HOCKEY_TEAM_FULL_GAME_TOTAL": 2,
                                   "HOCKEY_TEAM_FIRST_PERIOD_TOTAL": 1}
    assert nhl["main_lines_in_horizon"] >= 2       # winner + main total at least (periods depend on config)
