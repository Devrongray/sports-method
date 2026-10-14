"""The Odds API v4 client, filtered to Pinnacle, quota-aware.

    GET https://api.the-odds-api.com/v4/sports/{sport_key}/odds
        ?apiKey=...&regions=eu&markets=h2h,totals&bookmakers=pinnacle
        &oddsFormat=decimal&dateFormat=iso

Each call costs 1 credit per market per region (2 credits for h2h,totals in
one region). Quota comes back in the response headers x-requests-remaining,
x-requests-used and x-requests-last. GET /v4/sports is free.

Pinnacle is served in region "eu". The Odds API does not carry CS2/LoL;
`pinnacle_esports()` is a hook for a second feed (e.g. OddsPapi) and raises
until one is wired in.
"""
from __future__ import annotations

import os
from datetime import datetime, timezone
from typing import Iterator

import requests

BASE = "https://api.the-odds-api.com/v4"


class OddsAPI:
    def __init__(self, api_key: str | None = None, timeout: float = 20.0):
        self.api_key = api_key or os.environ.get("ODDS_API_KEY")
        if not self.api_key:
            raise RuntimeError("ODDS_API_KEY is not set")
        self.timeout = timeout
        self.quota = {"remaining": None, "used": None, "last": None}
        self.http = requests.Session()

    def _get(self, path: str, params: dict) -> list | dict:
        params = {"apiKey": self.api_key, **params}
        r = self.http.get(BASE + path, params=params, timeout=self.timeout)
        for k in ("remaining", "used", "last"):
            v = r.headers.get(f"x-requests-{k}")
            if v is not None:
                try:
                    self.quota[k] = float(v)
                except ValueError:
                    pass
        r.raise_for_status()
        return r.json()

    def sports(self) -> list[dict]:
        """Free call; also refreshes the quota headers."""
        return self._get("/sports", {})

    def odds(self, sport_key: str, markets: tuple[str, ...] = ("h2h", "totals"),
             regions: str = "eu", bookmakers: tuple[str, ...] = ("pinnacle",)) -> list[dict]:
        return self._get(f"/sports/{sport_key}/odds", {
            "regions": regions,
            "markets": ",".join(markets),
            "bookmakers": ",".join(bookmakers),
            "oddsFormat": "decimal",
            "dateFormat": "iso",
        })

    def pinnacle_esports(self, title: str) -> list[dict]:
        raise NotImplementedError(
            "The Odds API has no CS2/LoL; wire a Pinnacle esports feed (e.g. OddsPapi) here"
        )


def normalize_odds(events: list[dict], sport_key: str, recorded_at: str | None = None) -> Iterator[dict]:
    """One row per bookmaker × market × outcome."""
    ts = recorded_at or datetime.now(timezone.utc).isoformat(timespec="seconds")
    for ev in events:
        for bk in ev.get("bookmakers") or []:
            for mk in bk.get("markets") or []:
                for oc in mk.get("outcomes") or []:
                    yield {
                        "ts": ts,
                        "sport_key": sport_key,
                        "event_id": ev.get("id"),
                        "commence_time": ev.get("commence_time"),
                        "home": ev.get("home_team"),
                        "away": ev.get("away_team"),
                        "bookmaker": bk.get("key"),
                        "bookmaker_last_update": bk.get("last_update"),
                        "market": mk.get("key"),
                        "market_last_update": mk.get("last_update"),
                        "outcome": oc.get("name"),
                        "price": oc.get("price"),
                        "point": oc.get("point"),
                    }


def two_way_fair(rows: list[dict], method: str = "additive") -> list[dict]:
    """De-vig h2h pairs (and totals over/under pairs) from normalized rows."""
    from .devig import devig  # local import keeps this module import-light

    by_key: dict[tuple, list[dict]] = {}
    for r in rows:
        key = (r["event_id"], r["bookmaker"], r["market"], r.get("point"))
        by_key.setdefault(key, []).append(r)
    out = []
    for key, group in by_key.items():
        prices = [g["price"] for g in group if g.get("price")]
        if len(prices) != len(group) or len(prices) < 2:
            continue
        fair = devig(prices, method)
        for g, p in zip(group, fair):
            out.append({**g, "fair_prob": float(p), "devig_method": method})
    return out
