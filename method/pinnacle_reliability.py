"""Test (c): Pinnacle closing-price reliability by season, and de-vig choice.

Data: football-data.co.uk season files (free). Columns used:
    FTR                 result H/D/A
    PSCH, PSCD, PSCA    Pinnacle closing odds (present from 2019/20)
    PSH, PSD, PSA       Pinnacle odds collected before close (for the
                        opening-vs-closing comparison when present)

Pre-registered criteria (Method v1, test (c)):
    pass if every season's pooled calibration slope lies in 0.95–1.05;
    adopt the de-vig method with the lowest log loss.

    python -m method.pinnacle_reliability --out analysis/test_c            # downloads
    python -m method.pinnacle_reliability --local-dir csvs --out analysis/test_c
"""
from __future__ import annotations

import argparse
import io
import json
from pathlib import Path

import numpy as np
import pandas as pd
import requests

from .devig import METHODS, devig
from .metrics import calibration_fit, log_loss, murphy_decomposition

URL = "https://www.football-data.co.uk/mmz4281/{season}/{league}.csv"
SEASONS = ["1920", "2021", "2122", "2223", "2324", "2425", "2526"]
LEAGUES = {"E0": "England Premier League", "SP1": "Spain La Liga", "D1": "Germany Bundesliga",
           "I1": "Italy Serie A", "F1": "France Ligue 1"}
OUTCOMES = ["H", "D", "A"]


def season_label(code: str) -> str:
    return f"20{code[:2]}/{code[2:]}"


def fetch_csv(season: str, league: str, timeout: float = 30) -> pd.DataFrame | None:
    r = requests.get(URL.format(season=season, league=league), timeout=timeout)
    if r.status_code != 200 or not r.content:
        return None
    return parse_csv(r.content)


def parse_csv(content: bytes) -> pd.DataFrame:
    return pd.read_csv(io.BytesIO(content), encoding="latin-1", on_bad_lines="skip")


def load_local(local_dir: Path) -> list[tuple[str, str, pd.DataFrame]]:
    """Files named <season>_<league>.csv, e.g. 2324_E0.csv."""
    out = []
    for f in sorted(local_dir.glob("*.csv")):
        stem = f.stem
        if "_" in stem:
            season, league = stem.split("_", 1)
        else:
            season, league = "unknown", stem
        out.append((season, league.upper(), parse_csv(f.read_bytes())))
    return out


def prepare(df: pd.DataFrame, prefix: str = "PSC") -> pd.DataFrame:
    """Rows with a full set of odds and a result; adds q_H/q_D/q_A columns."""
    cols = [f"{prefix}H", f"{prefix}D", f"{prefix}A"]
    if not all(c in df.columns for c in cols) or "FTR" not in df.columns:
        return pd.DataFrame()
    d = df[cols + ["FTR"]].copy()
    for c in cols:
        d[c] = pd.to_numeric(d[c], errors="coerce")
    d = d.dropna()
    d = d[(d[cols] > 1.0).all(axis=1) & d["FTR"].isin(OUTCOMES)]
    # Guard against the kind of pricing error seen in the tennis-data file:
    # drop matches whose implied overround is outside a sane band.
    q = 1.0 / d[cols].to_numpy(float)
    over = q.sum(axis=1) - 1.0
    d = d[(over > -0.02) & (over < 0.15)]
    d = d.rename(columns={cols[0]: "oH", cols[1]: "oD", cols[2]: "oA"})
    return d.reset_index(drop=True)


def probabilities(d: pd.DataFrame, method: str) -> np.ndarray:
    odds = d[["oH", "oD", "oA"]].to_numpy(float)
    return np.vstack([devig(row, method) for row in odds])


def pooled_pairs(P: np.ndarray, results: pd.Series) -> tuple[np.ndarray, np.ndarray]:
    """Flatten (match, outcome) probabilities and indicators."""
    y = np.column_stack([(results == o).to_numpy(float) for o in OUTCOMES])
    return P.ravel(), y.ravel()


def evaluate(d: pd.DataFrame, method: str) -> dict:
    P = probabilities(d, method)
    p, y = pooled_pairs(P, d["FTR"])
    fit = calibration_fit(p, y)
    mur = murphy_decomposition(p, y, bins=10)
    # Log loss of the realised outcome's probability (multinomial form)
    idx = d["FTR"].map({o: i for i, o in enumerate(OUTCOMES)}).to_numpy()
    ll_multi = float(-np.mean(np.log(np.clip(P[np.arange(len(d)), idx], 1e-12, 1))))
    return {
        "method": method,
        "n_matches": int(len(d)),
        "log_loss_multinomial": ll_multi,
        "log_loss_binary_pooled": log_loss(p, y),
        "brier_pooled": mur.brier,
        "reliability": mur.reliability,
        "resolution": mur.resolution,
        "cal_slope": fit.slope,
        "cal_slope_se": fit.slope_se,
        "cal_intercept": fit.intercept,
        "mean_overround": float((1.0 / d[["oH", "oD", "oA"]].to_numpy(float)).sum(axis=1).mean() - 1.0),
    }


def run(frames: list[tuple[str, str, pd.DataFrame]], out: Path,
        slope_band: tuple[float, float] = (0.95, 1.05)) -> dict:
    out.mkdir(parents=True, exist_ok=True)
    rows = []
    by_season: dict[str, list[pd.DataFrame]] = {}
    for season, league, df in frames:
        d = prepare(df, "PSC")
        if d.empty:
            print(f"[skip] {season} {league}: no Pinnacle closing columns or no rows")
            continue
        by_season.setdefault(season, []).append(d)
        for m in METHODS:
            rows.append({"season": season_label(season), "league": league, **evaluate(d, m)})
        # Opening-vs-closing comparison when the pre-close columns exist
        o = prepare(df, "PS")
        if not o.empty:
            e = evaluate(o, "shin")
            rows.append({"season": season_label(season), "league": league, **e, "method": "shin_preclose"})

    pooled = []
    for season, parts in by_season.items():
        d = pd.concat(parts, ignore_index=True)
        for m in METHODS:
            e = evaluate(d, m)
            lo, hi = slope_band
            pooled.append({"season": season_label(season), "league": "ALL", **e,
                           "slope_in_band": bool(lo <= e["cal_slope"] <= hi)})

    res = pd.DataFrame(rows)
    pool = pd.DataFrame(pooled)
    res.to_csv(out / "by_league.csv", index=False)
    pool.to_csv(out / "pooled_by_season.csv", index=False)

    verdict = {}
    if not pool.empty:
        best = (pool.groupby("method")["log_loss_multinomial"].mean().sort_values())
        verdict["best_devig_method"] = str(best.index[0])
        verdict["mean_log_loss_by_method"] = {k: float(v) for k, v in best.items()}
        shin_rows = pool[pool["method"] == "shin"]
        verdict["seasons_slope_in_band"] = {r["season"]: bool(r["slope_in_band"]) for _, r in shin_rows.iterrows()}
        verdict["pass"] = bool(shin_rows["slope_in_band"].all()) if len(shin_rows) else None
        verdict["slope_band"] = list(slope_band)
    with open(out / "verdict.json", "w") as f:
        json.dump(verdict, f, indent=2)
    write_summary(out, pool, verdict)
    print(json.dumps(verdict, indent=2))
    return verdict


def write_summary(out: Path, pool: pd.DataFrame, verdict: dict) -> None:
    lines = ["# Test (c): Pinnacle closing-price reliability", ""]
    if pool.empty:
        lines.append("No seasons evaluated.")
    else:
        lines.append(f"Pass (shin slope within {verdict['slope_band']} every season): **{verdict.get('pass')}**. "
                     f"Lowest log loss: **{verdict.get('best_devig_method')}**.")
        lines += ["", "| Season | Method | Matches | Log loss | Brier | Slope (SE) | Intercept | Overround | In band |",
                  "|---|---|---|---|---|---|---|---|---|"]
        for _, r in pool.sort_values(["season", "method"]).iterrows():
            lines.append(f"| {r['season']} | {r['method']} | {r['n_matches']} | {r['log_loss_multinomial']:.4f} | "
                         f"{r['brier_pooled']:.4f} | {r['cal_slope']:.3f} ({r['cal_slope_se']:.3f}) | "
                         f"{r['cal_intercept']:+.3f} | {r['mean_overround']:.3%} | {'yes' if r['slope_in_band'] else 'no'} |")
    lines += ["", "Pooled over the top five leagues; calibration fitted on (match, outcome) pairs. "
              "Matches with an implied overround outside −2%…+15% are dropped as data errors."]
    (out / "summary.md").write_text("\n".join(lines) + "\n")


def main(argv: list[str] | None = None) -> None:
    p = argparse.ArgumentParser(prog="method.pinnacle_reliability")
    p.add_argument("--out", default="analysis/test_c")
    p.add_argument("--local-dir", help="directory of <season>_<league>.csv files instead of downloading")
    p.add_argument("--seasons", default=",".join(SEASONS))
    p.add_argument("--leagues", default=",".join(LEAGUES))
    args = p.parse_args(argv)
    frames: list[tuple[str, str, pd.DataFrame]] = []
    if args.local_dir:
        frames = load_local(Path(args.local_dir))
    else:
        for s in args.seasons.split(","):
            for lg in args.leagues.split(","):
                df = fetch_csv(s, lg)
                if df is None:
                    print(f"[miss] {s} {lg}")
                    continue
                frames.append((s, lg, df))
    run(frames, Path(args.out))


if __name__ == "__main__":
    main()
