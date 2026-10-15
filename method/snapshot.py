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
        print(f"{str(lg.get('slug')):<24} {str(lg.get('name')):<32} "
              f"operational={lg.get('isOperational')} sportId={lg.get('sportId')}")


def discover(client, cfg: dict, now: datetime) -> dict:
    """Live league list plus a check of every configured slug: does it exist,
    how many events, how many start within the horizon, which market types."""
    leagues = client.leagues() or []
    by_slug = {str(lg.get("slug")): lg for lg in leagues}
    horizon = timedelta(hours=cfg["cadence"]["horizon_hours"])
    checks = []
    for sp in cfg["sports"]:
        slug = sp["polymarket_league"]
        c = {"sport": sp["key"], "slug": slug, "slug_listed": slug in by_slug,
             "events": 0, "upcoming_in_horizon": 0, "market_types": {}, "market_classes": {},
             "main_lines_in_horizon": 0, "unclassified": [], "examples": {}, "error": None,
             "example_event": None}
        keep = set(sp["markets"])
        try:
            events = client.league_events(slug) or []
        except Exception as e:
            c["error"] = str(e)[:300]
            events = []
        c["events"] = len(events)
        for ev in events:
            start = pm.parse_iso(pm.event_start(ev))
            upcoming = bool(start and now <= start <= now + horizon and not (ev.get("ended") or ev.get("closed")))
            if upcoming:
                c["upcoming_in_horizon"] += 1
                if c["example_event"] is None:
                    c["example_event"] = {"slug": ev.get("slug"), "title": ev.get("title"), "start": pm.event_start(ev)}
            markets = ev.get("markets") or []
            parsed = pm.classify_event_markets(markets)
            mains = pm.mark_main_lines(markets, parsed)
            for m, (raw, cls, seg, scope), is_main in zip(markets, parsed, mains):
                c["market_types"][raw] = c["market_types"].get(raw, 0) + 1
                ck = f"{cls}/{seg}"
                c["market_classes"][ck] = c["market_classes"].get(ck, 0) + 1
                if cls == "OTHER" and raw not in c["unclassified"]:
                    c["unclassified"].append(raw)
                if upcoming and is_main and cls in keep:
                    c["main_lines_in_horizon"] += 1
                if raw not in c["examples"] or (is_main and not c["examples"][raw].get("is_main")):
                    c["examples"][raw] = {
                        "class": cls, "segment": seg, "is_main": is_main,
                        "question": m.get("question") or m.get("title"), "line": m.get("line"),
                        "slug": m.get("slug"),
                        "sides": [{"identifier": s.get("identifier"), "teamId": s.get("teamId"),
                                   "price": pm._amount(s.get("price"))} for s in (m.get("marketSides") or [])],
                    }
        checks.append(c)
    # Candidate slugs for anything that looks wrong: listed leagues whose slug or
    # name shares a token with the sport key or name.
    for c, sp in zip(checks, cfg["sports"]):
        if c["slug_listed"] and c["events"]:
            continue
        tokens = {sp["key"].lower(), *sp["name"].lower().replace("(", " ").replace(")", " ").split()}
        tokens -= {"only", "totals", "of", "the"}
        c["candidates"] = [s for s, lg in by_slug.items()
                           if any(t in s.lower() or t in str(lg.get("name", "")).lower() for t in tokens)][:15]
    return {"ts": now.isoformat(timespec="seconds"), "n_leagues": len(leagues),
            "leagues": [{"slug": lg.get("slug"), "name": lg.get("name"),
                         "isOperational": lg.get("isOperational"), "sportId": lg.get("sportId")} for lg in leagues],
            "checks": checks}


def cmd_discover(args) -> None:
    cfg = load_config(args.config)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    rep = discover(pm.PolymarketUS(), cfg, _utcnow())
    (out / "discovery.json").write_text(json.dumps(rep, indent=2, default=str) + "\n")
    lines = [f"# Polymarket US discovery {rep['ts']}", "",
             f"{rep['n_leagues']} leagues listed.", "",
             "| Sport | Slug | Listed | Events | Next 36h | Main lines to record (next 36h) | Unclassified types | Note |",
             "|---|---|---|---|---|---|---|---|"]
    for c in rep["checks"]:
        note = c["error"] or (", ".join(c.get("candidates", [])) and "candidates: " + ", ".join(c.get("candidates", [])))
        lines.append(f"| {c['sport']} | {c['slug']} | {'yes' if c['slug_listed'] else 'NO'} | {c['events']} | "
                     f"{c['upcoming_in_horizon']} | {c['main_lines_in_horizon']} | "
                     f"{', '.join(c['unclassified']) or '-'} | {note or ''} |")
    lines += ["", "## Market types seen, with one example each", "",
              "| Sport | Raw type | Class/segment | Count | Example question | Line | Sides |", "|---|---|---|---|---|---|---|"]
    for c in rep["checks"]:
        for raw, n in sorted(c["market_types"].items()):
            ex = c["examples"].get(raw, {})
            sides = "; ".join(f"{s['identifier']}{'' if s['teamId'] is None else ' (team ' + str(s['teamId']) + ')'}"
                              f"{'' if s['price'] is None else ' @' + format(s['price'], '.2f')}" for s in ex.get("sides", []))
            lines.append(f"| {c['sport']} | {raw} | {ex.get('class')}/{ex.get('segment')} | {n} | "
                         f"{str(ex.get('question') or '')[:60]} | {ex.get('line') if ex.get('line') is not None else ''} | {sides[:90]} |")
    lines += ["", "## All leagues", "", "| Slug | Name | Operational |", "|---|---|---|"]
    lines += [f"| {lg['slug']} | {lg['name']} | {lg['isOperational']} |" for lg in rep["leagues"]]
    (out / "summary.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines[:6 + len(rep["checks"])]))


# --- one pass ---------------------------------------------------------------

def _segments_for(cfg: dict) -> set[str] | None:
    """None = every segment; otherwise only the full game / match."""
    return None if cfg["cadence"].get("record_derivatives", True) else set(pm.MAIN_SEGMENTS)


def collect_markets_full(client: pm.PolymarketUS, cfg: dict, now: datetime) -> tuple[list[dict], list[dict]]:
    """Returns (kept, everything).

    kept:       main lines of the configured market classes, the rows that get
                BBO/book calls and price histories.
    everything: every market of every upcoming event (all classes, all
                alternate lines, with is_main flags), written once per pass
                because it costs nothing extra.
    """
    horizon = timedelta(hours=cfg["cadence"]["horizon_hours"])
    segments = _segments_for(cfg)
    kept: list[dict] = []
    everything: list[dict] = []
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
            mts = (start - now).total_seconds() / 60.0
            for row in pm.normalize_event_markets(ev, slug):
                row["sport"] = sp["key"]
                row["role"] = sp["role"]
                row["minutes_to_start"] = mts
                everything.append(row)
                if (row["market_class"] in keep and row["is_main"]
                        and (segments is None or row["segment"] in segments)):
                    kept.append(row)
    return kept, everything


def collect_markets(client: pm.PolymarketUS, cfg: dict, now: datetime) -> list[dict]:
    return collect_markets_full(client, cfg, now)[0]


def ladder_row(m: dict, ts: str) -> dict:
    """Compact per-line record for every market (all alternate lines) so the
    full ladder is kept each pass without repeating the event metadata."""
    return {"ts": ts, "sport": m["sport"], "event_id": m["event_id"], "start": m["start"],
            "market_slug": m["market_slug"], "market_type": m["market_type"],
            "market_class": m["market_class"], "segment": m["segment"], "line": m["line"],
            "is_main": m["is_main"], "mid": m.get("mid"),
            "bid": m.get("best_bid_quote"), "ask": m.get("best_ask_quote"),
            "minutes_to_start": round(m["minutes_to_start"], 1)}


def cmd_pass(args) -> dict:
    """One recording pass.

    scope "full"   (default, every polymarket_minutes): all upcoming events in the
                    horizon; writes markets_* (full rows, main lines), ladder_*
                    (compact rows, every line) and bbo_* for the main lines.
    scope "window" (every polymarket_window_minutes while a game is near): only
                    markets starting within the pre-start window; writes bbo_* and
                    books at the checkpoints. Keeps the data volume proportional
                    to what is actually changing.
    """
    cfg = load_config(args.config)
    out = Path(args.out)
    now = _utcnow()
    day = now.strftime("%Y-%m-%d")
    ts = now.isoformat(timespec="seconds")
    scope = getattr(args, "scope", "full") or "full"
    client = pm.PolymarketUS()

    window = cfg["cadence"]["pre_start_window_minutes"]
    checkpoints = cfg["cadence"]["book_checkpoints_minutes"]
    markets, everything = collect_markets_full(client, cfg, now)
    n_m = n_l = 0
    if scope == "full":
        for m in markets:
            m["ts"] = ts
        n_m = _write_ndjson(out / "polymarket" / day / f"markets_{_stamp(now)}.ndjson.gz", markets)
        n_l = _write_ndjson(out / "polymarket" / day / f"ladder_{_stamp(now)}.ndjson.gz",
                            [ladder_row(m, ts) for m in everything])
    else:
        markets = [m for m in markets if 0 <= m["minutes_to_start"] <= window]

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
        ctx = {"ts": ts, "sport": m["sport"], "event_id": m["event_id"], "start": m["start"],
               "market_type": m["market_type"], "market_class": m["market_class"], "segment": m["segment"],
               "line": m["line"], "minutes_to_start": round(m["minutes_to_start"], 2)}
        if md:
            bbo_rows.append({**ctx, **pm.normalize_bbo(md)})
        mts = m["minutes_to_start"]
        near_checkpoint = any(abs(mts - c) <= cfg["cadence"]["polymarket_window_minutes"] for c in checkpoints)
        if 0 <= mts <= window and near_checkpoint and m["segment"] in pm.MAIN_SEGMENTS:
            try:
                bk = client.book(slug)
            except Exception as e:
                print(f"[warn] book {slug}: {e}")
                bk = None
            if bk:
                book_rows.append({**ctx, **pm.normalize_book(bk)})
    tag = "" if scope == "full" else "w"
    n_b = _write_ndjson(out / "polymarket" / day / f"bbo{tag}_{_stamp(now)}.ndjson.gz", bbo_rows) if bbo_rows else 0
    n_k = _write_ndjson(out / "polymarket" / day / f"book_{_stamp(now)}.ndjson.gz", book_rows) if book_rows else 0

    n_p = 0
    if not getattr(args, "skip_pinnacle", False) and os.environ.get("ODDS_API_KEY"):
        n_p = pinnacle_pass(cfg, out, now, ts)
    by_sport: dict[str, int] = {}
    for m in markets:
        by_sport[m["sport"]] = by_sport.get(m["sport"], 0) + 1
    summary = {"ts": ts, "scope": scope, "markets_main": n_m, "ladder_rows": n_l, "bbo": n_b, "books": n_k,
               "pinnacle_rows": n_p, "by_sport": by_sport,
               "min_mts": sorted({round(m["minutes_to_start"], 1) for m in markets})[:3],
               "near_sports": sorted({m["sport"] for m in markets if 0 <= m["minutes_to_start"] <= window})}
    print(json.dumps(summary))
    return summary


def pinnacle_pass(cfg: dict, out: Path, now: datetime, ts: str, sports: list[str] | None = None) -> int:
    api = OddsAPI()
    oc = cfg["odds_api"]
    rows: list[dict] = []
    polled: list[str] = []
    for sp in cfg["sports"]:
        key = sp.get("odds_api_sport")
        if not key or (sports is not None and sp["key"] not in sports):
            continue
        if sp.get("role") == "benchmark" and not oc.get("include_benchmark", False):
            continue
        try:
            events = api.odds(key, tuple(oc["markets"]), oc["regions"], tuple(oc["bookmakers"]))
            polled.append(sp["key"])
        except Exception as e:
            print(f"[warn] odds api {key}: {e}")
            continue
        for r in normalize_odds(events, key, ts):
            r["sport"] = sp["key"]
            rows.append(r)
    day = now.strftime("%Y-%m-%d")
    n = _write_ndjson(out / "pinnacle" / day / f"odds_{_stamp(now)}.ndjson.gz", rows)
    meta = {"ts": ts, "pinnacle_rows": n, "sports": polled, "quota": api.quota}
    _write_json(out / "pinnacle" / day / f"quota_{_stamp(now)}.json.gz", meta)
    print(json.dumps(meta))
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
    segments = _segments_for(cfg)
    by_sport = {sp["key"]: sp for sp in cfg["sports"]}

    # 1. Markets we recorded ourselves (the event list drops games once they end,
    #    so finished games are only reachable this way).
    targets: dict[str, dict] = {}
    if args.recorded:
        for row in recorded_main_markets(Path(args.recorded), since, now):
            sp = by_sport.get(row["sport"])
            if sp and row["market_class"] in set(sp["markets"]) and (segments is None or row["segment"] in segments):
                targets[row["market_slug"]] = row
    n_recorded = len(targets)
    # 2. Whatever Polymarket still lists (catches anything the recorder missed).
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
            for row in pm.normalize_event_markets(ev, slug, keep, segments, main_only=True):
                if row.get("market_slug") and row["market_slug"] not in targets:
                    row["sport"] = sp["key"]
                    targets[row["market_slug"]] = row

    done = 0
    for mslug, row in targets.items():
        start = pm.parse_iso(row["start"])
        if start is None:
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
            "sport": row["sport"], "league": row.get("league"),
            "event_id": row["event_id"], "event_slug": row.get("event_slug"),
            "event_title": row.get("event_title"), "start": row["start"], "teams": row.get("teams"),
            "market_slug": mslug, "market_type": row["market_type"],
            "market_class": row["market_class"], "segment": row["segment"], "line": row.get("line"),
            "sides": row.get("sides"), "fee_coefficient": row.get("fee_coefficient"),
            "window_start_ts": s, "window_end_ts": e,
            "last_pregame": close, "settlement": settle, "n_points": len(hist),
            "history": hist,
        }
        day = start.strftime("%Y-%m-%d")
        _write_json(out / "polymarket_history" / day / f"{mslug}.json.gz", doc)
        done += 1
    print(json.dumps({"ts": now.isoformat(timespec="seconds"), "targets": len(targets),
                      "from_recorded": n_recorded, "histories_written": done}))


def recorded_main_markets(data: Path, since: datetime, until: datetime) -> list[dict]:
    """Latest recorded row of every main market whose game started in [since, until],
    read from the markets_* files on the data branch."""
    latest: dict[str, dict] = {}
    for day in sorted((data / "polymarket").glob("*")) if (data / "polymarket").exists() else []:
        for f in sorted(day.glob("markets_*.ndjson.gz")):
            with gzip.open(f, "rt", encoding="utf-8") as fh:
                for line in fh:
                    r = json.loads(line)
                    start = pm.parse_iso(r.get("start"))
                    if start is None or not (since <= start <= until) or not r.get("is_main"):
                        continue
                    latest[r["market_slug"]] = r
    return list(latest.values())


# --- loop --------------------------------------------------------------------

def cmd_loop(args) -> None:
    """Repeat `pass` for --minutes, at the window cadence when a game is near."""
    cfg = load_config(args.config)
    cad = cfg["cadence"]
    end = time.monotonic() + args.minutes * 60
    last_full = last_window = last_odds_all = last_odds_near = -1e9
    near_sports: list[str] = []
    while time.monotonic() < end:
        now = _utcnow()
        t = time.monotonic()
        args.skip_pinnacle = True
        if t - last_full >= cad["polymarket_minutes"] * 60:
            args.scope = "full"
            summary = cmd_pass(args)
            last_full = last_window = time.monotonic()
            near_sports = summary.get("near_sports", [])
        elif near_sports and t - last_window >= cad["polymarket_window_minutes"] * 60:
            args.scope = "window"
            summary = cmd_pass(args)
            last_window = time.monotonic()
            near_sports = summary.get("near_sports", [])
        if os.environ.get("ODDS_API_KEY"):
            ts = now.isoformat(timespec="seconds")
            if t - last_odds_all >= cad["odds_api_minutes"] * 60:
                pinnacle_pass(cfg, Path(args.out), now, ts)          # every sport
                last_odds_all = last_odds_near = time.monotonic()
            elif near_sports and t - last_odds_near >= cad["odds_api_window_minutes"] * 60:
                pollable = [s["key"] for s in cfg["sports"] if s.get("odds_api_sport") and s["key"] in near_sports
                            and (s.get("role") != "benchmark" or cfg["odds_api"].get("include_benchmark"))]
                if pollable:
                    pinnacle_pass(cfg, Path(args.out), now, ts, sports=pollable)   # only sports with a game near
                last_odds_near = time.monotonic()
        time.sleep(15)


def main(argv: list[str] | None = None) -> None:
    p = argparse.ArgumentParser(prog="method.snapshot")
    p.add_argument("--config", default=str(CONFIG))
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("leagues").set_defaults(fn=cmd_leagues)
    sd = sub.add_parser("discover")
    sd.add_argument("--out", default="analysis/discovery")
    sd.set_defaults(fn=cmd_discover)
    sp = sub.add_parser("pass")
    sp.add_argument("--out", default="data")
    sp.add_argument("--scope", choices=["full", "window"], default="full")
    sp.add_argument("--skip-pinnacle", action="store_true")
    sp.set_defaults(fn=cmd_pass)
    sh = sub.add_parser("history")
    sh.add_argument("--out", default="data")
    sh.add_argument("--hours", type=float, default=24, help="games that started within the last N hours")
    sh.add_argument("--before", type=float, default=12, help="hours of history before start")
    sh.add_argument("--after", type=float, default=6, help="hours after start")
    sh.add_argument("--recorded", default=None, help="data dir (data branch checkout) to take recorded market slugs from")
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
