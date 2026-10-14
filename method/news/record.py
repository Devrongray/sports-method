"""Loop the news recorders for --minutes.

    python -m method.news.record --out data --minutes 27
"""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

from .common import utcnow
from .mlb import MLBLineups
from .nba import NBAInjuryReports
from .nhl import NHLGoalies


def main(argv=None) -> None:
    p = argparse.ArgumentParser(prog="method.news.record")
    p.add_argument("--out", default="data")
    p.add_argument("--minutes", type=float, default=27)
    p.add_argument("--mlb-every", type=float, default=2, help="minutes")
    p.add_argument("--nba-every", type=float, default=5, help="minutes")
    p.add_argument("--nhl-every", type=float, default=5, help="minutes")
    args = p.parse_args(argv)
    out = Path(args.out)
    rec = {"mlb": (MLBLineups(out), args.mlb_every), "nba": (NBAInjuryReports(out), args.nba_every),
           "nhl": (NHLGoalies(out), args.nhl_every)}
    last = {k: -1e9 for k in rec}
    end = time.monotonic() + args.minutes * 60
    while time.monotonic() < end:
        t = time.monotonic()
        for k, (r, every) in rec.items():
            if t - last[k] >= every * 60:
                try:
                    print(json.dumps({"source": k, **r.poll(utcnow())}))
                except Exception as e:
                    print(f"[warn] {k}: {e}")
                last[k] = time.monotonic()
        time.sleep(10)


if __name__ == "__main__":
    main()
