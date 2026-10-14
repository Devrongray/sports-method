"""Polymarket US public gateway client (no API key).

Endpoints used (docs.polymarket.us, read 14 Oct 2026):
    GET /v2/leagues                       leagues with slugs (max 50 per page)
    GET /v2/leagues/{slug}/events         events + nested markets for a league
    GET /v1/markets/{slug}/bbo            best bid/offer and resting shares
    GET /v1/markets/{slug}/book           full order book (price levels)
    GET /v1/price-history                 stored observations, fidelity 1 = minute
    GET /v1/markets/{slug}/settlement     settlement price once resolved

Prices are contract prices in dollars (0–1). Price history gives
longPrice ≈ best ask (Yes) and shortPrice ≈ 1 − best bid (Yes); they can sum
to more than one because the spread is preserved. Rate limit on price
history: 20 requests/second/IP.

Field names follow the published OpenAPI spec. The spec carries no example
payloads, so the normalisers below read defensively and keep the raw
objects alongside the parsed fields.
"""
from __future__ import annotations

import time
from datetime import datetime, timezone
from typing import Any, Iterator

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

BASE = "https://gateway.polymarket.us"
MARKET_TYPE_PREFIX = "SPORTS_MARKET_TYPE_"


def _session() -> requests.Session:
    s = requests.Session()
    retry = Retry(total=4, backoff_factor=0.5, status_forcelist=(429, 500, 502, 503, 504),
                  allowed_methods=("GET",))
    s.mount("https://", HTTPAdapter(max_retries=retry))
    s.headers["User-Agent"] = "sports-method/0.1 (research; contact via repo)"
    return s


def _amount(x: Any) -> float | None:
    """Parse an Amount {value, currency}, a bare number, or a numeric string."""
    if x is None:
        return None
    if isinstance(x, dict):
        x = x.get("value")
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def _num(x: Any) -> float | None:
    try:
        return None if x is None else float(x)
    except (TypeError, ValueError):
        return None


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


class PolymarketUS:
    def __init__(self, base: str = BASE, timeout: float = 20.0, min_interval: float = 0.06):
        self.base = base.rstrip("/")
        self.timeout = timeout
        self.min_interval = min_interval  # ~16 req/s, under the 20/s limit
        self._last = 0.0
        self.http = _session()

    # --- low level -----------------------------------------------------
    def _get(self, path: str, params: dict | None = None) -> Any | None:
        wait = self.min_interval - (time.monotonic() - self._last)
        if wait > 0:
            time.sleep(wait)
        r = self.http.get(self.base + path, params=params, timeout=self.timeout)
        self._last = time.monotonic()
        if r.status_code == 404:
            return None
        r.raise_for_status()
        return r.json()

    # --- discovery -----------------------------------------------------
    def leagues(self) -> list[dict]:
        out: list[dict] = []
        offset = 0
        while True:
            data = self._get("/v2/leagues", {"limit": 50, "offset": offset}) or {}
            batch = data.get("leagues") or []
            out.extend(batch)
            if len(batch) < 50:
                return out
            offset += 50

    def league_events(self, league_slug: str, type_: str = "sport", page: int = 50) -> list[dict]:
        out: list[dict] = []
        offset = 0
        while True:
            data = self._get(f"/v2/leagues/{league_slug}/events",
                             {"type": type_, "limit": page, "offset": offset})
            if data is None:
                return out
            batch = data.get("events") or []
            out.extend(batch)
            if len(batch) < page:
                return out
            offset += page

    # --- market data ---------------------------------------------------
    def bbo(self, market_slug: str) -> dict | None:
        data = self._get(f"/v1/markets/{market_slug}/bbo")
        return None if data is None else (data.get("marketData") or data)

    def book(self, market_slug: str) -> dict | None:
        data = self._get(f"/v1/markets/{market_slug}/book")
        return None if data is None else (data.get("marketData") or data)

    def price_history(self, market_slug: str, start_ts: int, end_ts: int, fidelity: int = 1) -> list[dict]:
        """Stored observations between two Unix-second timestamps (≤ ~24h)."""
        data = self._get("/v1/price-history", {
            "symbol": market_slug,
            "timestamp.startTimestamp": int(start_ts),
            "timestamp.endTimestamp": int(end_ts),
            "fidelity": fidelity,
        }) or {}
        return data.get("history") or []

    def price_history_interval(self, market_slug: str, interval: str = "INTERVAL_1D", fidelity: int = 5) -> list[dict]:
        data = self._get("/v1/price-history", {
            "symbol": market_slug, "fixedInterval": interval, "fidelity": fidelity,
        }) or {}
        return data.get("history") or []

    def settlement(self, market_slug: str) -> float | None:
        data = self._get(f"/v1/markets/{market_slug}/settlement")
        if not data:
            return None
        return _num(data.get("settlement"))


# --- normalisers ---------------------------------------------------------

def market_type(m: dict) -> str:
    t = m.get("sportsMarketType") or m.get("sportsMarketTypeV2") or m.get("marketType") or ""
    t = str(t).upper()
    if t.startswith(MARKET_TYPE_PREFIX):
        t = t[len(MARKET_TYPE_PREFIX):]
    aliases = {"MONEYLINE": "MONEYLINE", "SPREADS": "SPREAD", "SPREAD": "SPREAD",
               "TOTALS": "TOTAL", "TOTAL": "TOTAL", "PROP": "PROP", "FUTURE": "FUTURE",
               "DRAWABLE_OUTCOME": "DRAWABLE_OUTCOME"}
    return aliases.get(t, t or "UNKNOWN")


def event_start(ev: dict) -> str | None:
    for k in ("startTime", "startDate", "eventDate"):
        if ev.get(k):
            return ev[k]
    return None


def parse_iso(s: str | None) -> datetime | None:
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError:
        return None


def normalize_event_markets(ev: dict, league_slug: str, keep_types: set[str] | None = None) -> Iterator[dict]:
    """One row per market of an event, with its sides and the event context."""
    start = event_start(ev)
    teams = [{"id": t.get("id"), "name": t.get("name"), "abbr": t.get("abbreviation")}
             for t in (ev.get("teams") or [])]
    for m in ev.get("markets") or []:
        mt = market_type(m)
        if keep_types and mt not in keep_types:
            continue
        sides = []
        for s in m.get("marketSides") or []:
            sides.append({
                "id": s.get("id"),
                "type": s.get("marketSideType"),
                "identifier": s.get("identifier"),
                "price": _amount(s.get("price")),
                "long": s.get("long"),
                "team_id": s.get("teamId"),
                "tradable": s.get("tradable"),
            })
        yield {
            "league": league_slug,
            "event_id": ev.get("id"),
            "event_slug": ev.get("slug"),
            "event_title": ev.get("title"),
            "start": start,
            "live": ev.get("live"),
            "ended": ev.get("ended"),
            "closed": ev.get("closed"),
            "teams": teams,
            "market_id": m.get("id"),
            "market_slug": m.get("slug"),
            "market_type": mt,
            "question": m.get("question") or m.get("title"),
            "line": _num(m.get("line")),
            "active": m.get("active"),
            "market_closed": m.get("closed"),
            "fee_coefficient": _num(m.get("feeCoefficient")),
            "tick": _num(m.get("orderPriceMinTickSize")),
            "best_bid_quote": _amount(m.get("bestBidQuote")),
            "best_ask_quote": _amount(m.get("bestAskQuote")),
            "volume": _num(m.get("volume")),
            "sides": sides,
        }


def normalize_bbo(md: dict) -> dict:
    bid = _amount(md.get("bestBid"))
    ask = _amount(md.get("bestAsk"))
    mid = (bid + ask) / 2 if bid is not None and ask is not None else None
    sample = md.get("lastPriceSample") or {}
    return {
        "market_slug": md.get("marketSlug"),
        "best_bid": bid,
        "best_ask": ask,
        "mid": mid,
        "spread": (ask - bid) if bid is not None and ask is not None else None,
        "bid_shares": _num(md.get("bidShares")),
        "ask_shares": _num(md.get("askShares")),
        "bid_depth_levels": md.get("bidDepth"),
        "ask_depth_levels": md.get("askDepth"),
        "current_px": _amount(md.get("currentPx")),
        "last_trade_px": _amount(md.get("lastTradePx")),
        "settlement_px": _amount(md.get("settlementPx")),
        "shares_traded": _num(md.get("sharesTraded")),
        "open_interest": _num(md.get("openInterest")),
        "state": md.get("state"),
        "sample_long": _amount(sample.get("longPx")),
        "sample_short": _amount(sample.get("shortPx")),
        "sample_ts": sample.get("ts"),
    }


def normalize_book(md: dict, levels: int = 10) -> dict:
    def side(entries):
        out = []
        for e in (entries or [])[:levels]:
            out.append({"px": _amount(e.get("px")), "qty": _num(e.get("qty"))})
        return out
    stats = md.get("stats") or {}
    return {
        "market_slug": md.get("marketSlug"),
        "bids": side(md.get("bids")),
        "offers": side(md.get("offers")),
        "state": md.get("state"),
        "transact_time": md.get("transactTime"),
        "last_trade_px": _amount(stats.get("lastTradePx")),
        "shares_traded": _num(stats.get("sharesTraded")),
        "open_interest": _num(stats.get("openInterest")),
    }


def normalize_history(points: list[dict]) -> list[dict]:
    """Derive bid/ask/mid from the long/short display prices."""
    rows = []
    for pt in points:
        long_ = _num(pt.get("longPrice"))
        short = _num(pt.get("shortPrice"))
        bid = (1.0 - short) if short is not None else None
        ask = long_
        mid = (bid + ask) / 2 if bid is not None and ask is not None else None
        rows.append({
            "timestamp": int(pt.get("timestamp")) if pt.get("timestamp") is not None else None,
            "long_price": long_,
            "short_price": short,
            "best_bid": bid,
            "best_ask": ask,
            "mid": mid,
            "spread": (ask - bid) if bid is not None and ask is not None else None,
        })
    return rows


def last_pregame_mid(history_rows: list[dict], start: datetime, cutoff_seconds: int = 60) -> dict | None:
    """The last observation at least `cutoff_seconds` before the start time.

    This is the CLV benchmark for a Polymarket US position (fee-adjusted entry
    price vs. last pre-game mid).
    """
    cutoff = int(start.timestamp()) - cutoff_seconds
    best = None
    for r in history_rows:
        if r["timestamp"] is not None and r["timestamp"] <= cutoff and r.get("mid") is not None:
            if best is None or r["timestamp"] > best["timestamp"]:
                best = r
    return best
