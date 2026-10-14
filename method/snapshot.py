"""Recorder for the data phase.

    python -m method.snapshot leagues                 print Polymarket US league slugs
    python -m method.snapshot pass --out data         one pass: markets, BBO, books, Pinnacle
    python -m method.snapshot history --out data      price paths + settlement for games that started in the last --hours
    python -m method.snapshot loop --out data --minutes 28   repeat `pass` on the configured cadence

Output: gzipped NDJSON per pass under data/<source>/<YYYY-MM-DD>/, one JSON
document per line, each with `ts` (UTC, our clock) plus the venue timestamp.
"""
from __future__ import annotations

import argparse
import gzip
import json
import os
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import yaml

from . import polymarket_us as pm
from .odds_api import OddsAPI, normalize_odds

CONFIG = Path(__file__).resolve().parent.parent / "config" / "sports.yaml"


def load_config(path: Path = CONFIG) -> dict:
    with open(path) as f:
        return yaml.safe_load(f)


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


def _stamp(dt: datetime) -> str:
    return dt.strftime("%Y%m%dT%H%M%SZ")


def _write_ndjson(path: Path, rows: list[dict]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(path, "wt", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, separators=(",", ":"), default=str) + "\n")
    return len(rows)


def _write_json(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(path, "wt", encoding="utf-8") as f:
        json.dump(obj, f, separators=(",", ":"), default=str)


# --- discovery -------------------------------------------------------------

def cmd_leagues(args) -> None:
    client = pm.PolymarketUS()
    for lg in client.leagues():
        print(f"{lg.get('slug'):<24} {lg.get('name'):<32} operational={lg.get('isOperational')} sportId={lg.get('sportId')}")


# --- one pass ---------------------------------------------------------------

def collect_markets(client: pm.PolymarketUS, cfg: dict, now: datetime) -> list[dict]:
    horizon = timedelta(hours=cfg["cadence"]["horizon_hours"])
    rows: list[dict] = []
    for sp in cfg["sports"]:
        slug = sp["polymarket_league"]
        keep = set(sp["markets"])
        try:
            events = client.league_events(slug)
        except Exception as e:  # keep the pass alive if one league fails
            print(f"[warn] league {slug}: {e}")
            continue
        for ev in events:
            start = pm.parse_iso(pm.event_start(ev))
            if start is None:
                continue
            if start > now + horizon:
                continue
            if ev.get("ended") or ev.get("closed"):
                continue
            for row in pm.normalize_event_markets(ev, slug, keep):
                row["sport"] = sp["key"]
                row["role"] = sp["role"]
                row["minutes_to_start"] = (start - now).total_seconds() / 60.0
                rows.append(row)
    return rows


def cmd_pass(args) -> dict:
    cfg = load_config(args.config)
    out = Path(args.out)
    now = _utcnow()
    day = now.strftime("%Y-%m-%d")
    ts = now.isoformat(timespec="seconds")
    client = pm.PolymarketUS()

    markets = collect_markets(client, cfg, now)
    for m in markets:
        m["ts"] = ts
    n_m = _write_ndjson(out / "polymarket" / day / f"markets_{_stamp(now)}.ndjson.gz", markets)

    window = cfg["cadence"]["pre_start_window_minutes"]
    checkpoints = cfg["cadence"]["book_checkpoints_minutes"]
    bbo_rows, book_rows = [], []
    for m in markets:
        slug = m.get("market_slug")
        if not slug:
            continue
        try:
            md = client.bbo(slug)
        except Exception as e:
            print(f"[warn] bbo {slug}: {e}")
            continue
        if md:
            bbo_rows.append({"ts": ts, "sport": m["sport"], "event_id": m["event_id"], "start": m["start"],
                             "market_type": m["market_type"], "line": m["line"],
                             "minutes_to_start": round(m["minutes_to_start"], 2), **pm.normalize_bbo(md)})
        mts = m["minutes_to_start"]
        near_checkpoint = any(abs(mts - c) <= cfg["cadence"]["polymarket_window_minutes"] for c in checkpoints)
        if 0 <= mts <= window and near_checkpoint:
            try:
                bk = client.book(slug)
            except Exception as e:
                print(f"[warn] book {slug}: {e}")
                bk = None
            if bk:
                book_rows.append({"ts": ts, "sport": m["sport"], "event_id": m["event_id"], "start": m["start"],
                                  "market_type": m["market_type"], "line": m["line"],
                                  "minutes_to_start": round(mts, 2), **pm.normalize_book(bk)})
    n_b = _write_ndjson(out / "polymarket" / day / f"bbo_{_stamp(now)}.ndjson.gz", bbo_rows)
    n_k = _write_ndjson(out / "polymarket" / day / f"book_{_stamp(now)}.ndjson.gz", book_rows) if book_rows else 0

    n_p = 0
    if not args.skip_pinnacle and os.environ.get("ODDS_API_KEY"):
        n_p = pinnacle_pass(cfg, out, now, ts)
    summary = {"ts": ts, "markets": n_m, "bbo": n_b, "books": n_k, "pinnacle_rows": n_p}
    print(json.dumps(summary))
    return summary


def pinnacle_pass(cfg: dict, out: Path, now: datetime, ts: str, sports: list[str] | None = None) -> int:
    api = OddsAPI()
    oc = cfg["odds_api"]
    rows: list[dict] = []
    for sp in cfg["sports"]:
        key = sp.get("odds_api_sport")
        if not key or (sports and sp["key"] not in sports):
            continue
        try:
            events = api.odds(key, tuple(oc["markets"]), oc["regions"], tuple(oc["bookmakers"]))
        except Exception as e:
            print(f"[warn] odds api {key}: {e}")
            continue
        for r in normalize_odds(events, key, ts):
            r["sport"] = sp["key"]
            rows.append(r)
    day = now.strftime("%Y-%m-%d")
    n = _write_ndjson(out / "pinnacle" / day / f"odds_{_stamp(now)}.ndjson.gz", rows)
    print(json.dumps({"ts": ts, "pinnacle_rows": n, "quota": api.quota}))
    return n


# --- history ----------------------------------------------------------------

def cmd_history(args) -> None:
    """Minute-level price path and settlement for games that started in the window.

    Uses the custom-range price history (≤ 24h, fidelity 1), from `before`
    hours before start to `after` hours after. This is what the lag test (a)
    and the calibration test (b) consume.
    """
    cfg = load_config(args.config)
    out = Path(args.out)
    now = _utcnow()
    client = pm.PolymarketUS()
    since = now - timedelta(hours=args.hours)
    done = 0
    for sp in cfg["sports"]:
        slug = sp["polymarket_league"]
        keep = set(sp["markets"])
        try:
            events = client.league_events(slug)
        except Exception as e:
            print(f"[warn] league {slug}: {e}")
            continue
        for ev in events:
            start = pm.parse_iso(pm.event_start(ev))
            if start is None or not (since <= start <= now):
                continue
            for row in pm.normalize_event_markets(ev, slug, keep):
                mslug = row.get("market_slug")
                if not mslug:
                    continue
                s = int((start - timedelta(hours=args.before)).timestamp())
                e = int(min(start + timedelta(hours=args.after), now).timestamp())
                try:
                    hist = pm.normalize_history(client.price_history(mslug, s, e, 1))
                    settle = client.settlement(mslug)
                except Exception as ex:
                    print(f"[warn] history {mslug}: {ex}")
                    continue
                close = pm.last_pregame_mid(hist, start)
                doc = {
                    "ts": now.isoformat(timespec="seconds"),
                    "sport": sp["key"], "league": slug,
                    "event_id": row["event_id"], "event_slug": row["event_slug"],
                    "event_title": row["event_title"], "start": row["start"], "teams": row["teams"],
                    "market_slug": mslug, "market_type": row["market_type"], "line": row["line"],
                    "sides": row["sides"], "fee_coefficient": row["fee_coefficient"],
                    "window_start_ts": s, "window_end_ts": e,
                    "last_pregame": close, "settlement": settle, "n_points": len(hist),
                    "history": hist,
                }
                day = start.strftime("%Y-%m-%d")
                _write_json(out / "polymarket_history" / day / f"{mslug}.json.gz", doc)
                done += 1
    print(json.dumps({"ts": now.isoformat(timespec="seconds"), "histories_written": done}))


# --- loop --------------------------------------------------------------------

def cmd_loop(args) -> None:
    """Repeat `pass` for --minutes, at the window cadence when a game is near."""
    cfg = load_config(args.config)
    cad = cfg["cadence"]
    end = time.monotonic() + args.minutes * 60
    last_pm = last_odds = 0.0
    while time.monotonic() < end:
        now = _utcnow()
        client = pm.PolymarketUS()
        try:
            markets = collect_markets(client, cfg, now)
        except Exception as e:
            print(f"[warn] collect: {e}")
            markets = []
        near = any(0 <= m["minutes_to_start"] <= cad["pre_start_window_minutes"] for m in markets)
        pm_every = cad["polymarket_window_minutes"] if near else cad["polymarket_minutes"]
        odds_every = cad["odds_api_window_minutes"] if near else cad["odds_api_minutes"]
        t = time.monotonic()
        if t - last_pm >= pm_every * 60:
            args.skip_pinnacle = True
            cmd_pass(args)
            last_pm = time.monotonic()
        if os.environ.get("ODDS_API_KEY") and t - last_odds >= odds_every * 60:
            pinnacle_pass(cfg, Path(args.out), now, now.isoformat(timespec="seconds"))
            last_odds = time.monotonic()
        time.sleep(min(60, max(5, pm_every * 60 / 2)))


def main(argv: list[str] | None = None) -> None:
    p = argparse.ArgumentParser(prog="method.snapshot")
    p.add_argument("--config", default=str(CONFIG))
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("leagues").set_defaults(fn=cmd_leagues)
    sp = sub.add_parser("pass")
    sp.add_argument("--out", default="data")
    sp.add_argument("--skip-pinnacle", action="store_true")
    sp.set_defaults(fn=cmd_pass)
    sh = sub.add_parser("history")
    sh.add_argument("--out", default="data")
    sh.add_argument("--hours", type=float, default=24, help="games that started within the last N hours")
    sh.add_argument("--before", type=float, default=12, help="hours of history before start")
    sh.add_argument("--after", type=float, default=6, help="hours after start")
    sh.set_defaults(fn=cmd_history)
    sl = sub.add_parser("loop")
    sl.add_argument("--out", default="data")
    sl.add_argument("--minutes", type=float, default=28)
    sl.add_argument("--skip-pinnacle", action="store_true")
    sl.set_defaults(fn=cmd_loop)
    args = p.parse_args(argv)
    args.fn(args)


if __name__ == "__main__":
    main()
