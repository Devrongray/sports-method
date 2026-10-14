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

from math import erf, sqrt

from .devig import METHODS, devig
from .metrics import calibration_fit, log_loss, murphy_decomposition

URL = "https://www.football-data.co.uk/mmz4281/{season}/{league}.csv"
SEASONS = ["1920", "2021", "2122", "2223", "2324", "2425", "2526", "2627"]
EARLY = {"1920", "2021", "2122", "2223"}      # pre-registered split for the era comparison
LATE = {"2324", "2425", "2526", "2627"}
LEAGUES = {"E0": "England Premier League", "SP1": "Spain La Liga", "D1": "Germany Bundesliga",
           "I1": "Italy Serie A", "F1": "France Ligue 1"}
OUTCOMES = ["H", "D", "A"]


def season_label(code: str) -> str:
    return f"20{code[:2]}/{code[2:]}"


HEADERS = {"User-Agent": "Mozilla/5.0 (research; sports-method test c)"}


def fetch_csv(season: str, league: str, timeout: float = 30) -> pd.DataFrame | None:
    try:
        r = requests.get(URL.format(season=season, league=league), timeout=timeout, headers=HEADERS)
    except requests.RequestException as e:
        print(f"[error] {season} {league}: {e}")
        return None
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
    coverage = []
    by_season: dict[str, list[pd.DataFrame]] = {}
    for season, league, df in frames:
        d = prepare(df, "PSC")
        played = int(df["FTR"].isin(OUTCOMES).sum()) if "FTR" in df.columns else 0
        # Which closing-odds columns the file carries, and how complete each is:
        # Pinnacle (PSC), bet365 (B365C), market best (MaxC) and average (AvgC).
        closing_sets = {}
        for name, pref in (("pinnacle", "PSC"), ("bet365", "B365C"), ("max", "MaxC"), ("avg", "AvgC")):
            cols = [f"{pref}H", f"{pref}D", f"{pref}A"]
            if all(c in df.columns for c in cols) and played:
                ok = df[cols].apply(pd.to_numeric, errors="coerce").notna().all(axis=1)
                closing_sets[name] = round(float(ok.sum()) / played, 3)
            else:
                closing_sets[name] = None
        psc_dates = None
        if all(c in df.columns for c in ("PSCH", "Date")):
            has = pd.to_numeric(df["PSCH"], errors="coerce").notna()
            if has.any():
                psc_dates = f"{df.loc[has, 'Date'].iloc[0]} to {df.loc[has, 'Date'].iloc[-1]}"
        coverage.append({"season": season_label(season), "league": league, "rows_in_file": int(len(df)),
                         "matches_with_result": played, "matches_with_pinnacle_close": int(len(d)),
                         "share_with_close": (len(d) / played) if played else None,
                         "has_PSC_columns": all(c in df.columns for c in ("PSCH", "PSCD", "PSCA")),
                         "share_pinnacle": closing_sets["pinnacle"], "share_bet365": closing_sets["bet365"],
                         "share_max": closing_sets["max"], "share_avg": closing_sets["avg"],
                         "pinnacle_close_dates": psc_dates,
                         "last_date_in_file": str(df["Date"].iloc[-1]) if "Date" in df.columns and len(df) else None})
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
    cov = pd.DataFrame(coverage)
    res.to_csv(out / "by_league.csv", index=False)
    pool.to_csv(out / "pooled_by_season.csv", index=False)
    cov.to_csv(out / "coverage.csv", index=False)

    verdict = {}
    if not pool.empty:
        best = (pool.groupby("method")["log_loss_multinomial"].mean().sort_values())
        verdict["best_devig_method"] = str(best.index[0])
        verdict["mean_log_loss_by_method"] = {k: float(v) for k, v in best.items()}
        shin_rows = pool[pool["method"] == "shin"]
        verdict["seasons_slope_in_band"] = {r["season"]: bool(r["slope_in_band"]) for _, r in shin_rows.iterrows()}
        verdict["pass"] = bool(shin_rows["slope_in_band"].all()) if len(shin_rows) else None
        verdict["slope_band"] = list(slope_band)
        verdict["shin_slope_by_season"] = {r["season"]: [round(float(r["cal_slope"]), 4), round(float(r["cal_slope_se"]), 4)]
                                           for _, r in shin_rows.iterrows()}
        # How often this pass rule would fail if Pinnacle were perfectly calibrated,
        # given the standard errors actually observed (power check on the rule itself).
        lo, hi = slope_band
        p_all_in = 1.0
        for _, r in shin_rows.iterrows():
            se = float(r["cal_slope_se"])
            if se > 0:
                p_in = _norm_cdf((hi - 1.0) / se) - _norm_cdf((lo - 1.0) / se)
                p_all_in *= p_in
        verdict["false_fail_probability_if_calibrated"] = round(1.0 - p_all_in, 3)
        verdict["seasons_outside_2se_of_1"] = [r["season"] for _, r in shin_rows.iterrows()
                                                if abs(float(r["cal_slope"]) - 1.0) > 2 * float(r["cal_slope_se"])]
        # Era comparison: pooled early vs late seasons (split fixed in advance in EARLY/LATE)
        early = [d for sn, parts in by_season.items() if sn in EARLY for d in parts]
        late = [d for sn, parts in by_season.items() if sn in LATE for d in parts]
        if early and late:
            e_fit = evaluate(pd.concat(early, ignore_index=True), "shin")
            l_fit = evaluate(pd.concat(late, ignore_index=True), "shin")
            diff = l_fit["cal_slope"] - e_fit["cal_slope"]
            se_d = sqrt(e_fit["cal_slope_se"] ** 2 + l_fit["cal_slope_se"] ** 2)
            z = diff / se_d if se_d > 0 else float("nan")
            verdict["era_comparison"] = {
                "early_seasons": sorted(season_label(s) for s in by_season if s in EARLY),
                "late_seasons": sorted(season_label(s) for s in by_season if s in LATE),
                "early_slope": round(e_fit["cal_slope"], 4), "early_se": round(e_fit["cal_slope_se"], 4),
                "early_n": e_fit["n_matches"],
                "late_slope": round(l_fit["cal_slope"], 4), "late_se": round(l_fit["cal_slope_se"], 4),
                "late_n": l_fit["n_matches"],
                "late_minus_early": round(diff, 4), "z": round(z, 2),
                "two_sided_p": round(2 * (1 - _norm_cdf(abs(z))), 4) if z == z else None,
                "early_log_loss": round(e_fit["log_loss_multinomial"], 5),
                "late_log_loss": round(l_fit["log_loss_multinomial"], 5),
            }
    with open(out / "verdict.json", "w") as f:
        json.dump(verdict, f, indent=2)
    write_summary(out, pool, verdict)
    print(json.dumps(verdict, indent=2))
    return verdict


def _norm_cdf(x: float) -> float:
    return 0.5 * (1.0 + erf(x / sqrt(2.0)))


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
    if "false_fail_probability_if_calibrated" in verdict:
        lines += ["", "## Rule power check", "",
                  f"If Pinnacle were perfectly calibrated (slope exactly 1 every season), the pre-registered "
                  f"all-seasons-in-band rule would still fail with probability "
                  f"**{verdict['false_fail_probability_if_calibrated']:.0%}**, given the standard errors observed. "
                  f"Seasons whose slope differs from 1 by more than 2 SE: "
                  f"{', '.join(verdict['seasons_outside_2se_of_1']) or 'none'}."]
    ec = verdict.get("era_comparison")
    if ec:
        lines += ["", "## Era comparison (Shin de-vig, pooled)", "",
                  "| Era | Seasons | Matches | Slope (SE) | Log loss |", "|---|---|---|---|---|",
                  f"| Early | {', '.join(ec['early_seasons'])} | {ec['early_n']} | {ec['early_slope']:.3f} ({ec['early_se']:.3f}) | {ec['early_log_loss']:.4f} |",
                  f"| Late | {', '.join(ec['late_seasons'])} | {ec['late_n']} | {ec['late_slope']:.3f} ({ec['late_se']:.3f}) | {ec['late_log_loss']:.4f} |",
                  "", f"Late minus early slope: **{ec['late_minus_early']:+.3f}** (z = {ec['z']}, two-sided p = {ec['two_sided_p']})."]
    cov_path = out / "coverage.csv"
    if cov_path.exists():
        cov = pd.read_csv(cov_path)
        lines += ["", "## Data coverage", "",
                  "Share of played matches carrying each closing-odds set (Pinnacle = PSC columns, used by this test).", "",
                  "| Season | League | Played | Pinnacle | bet365 | Max | Avg | Pinnacle close dates | Last date in file |",
                  "|---|---|---|---|---|---|---|---|---|"]
        pct = lambda v: "" if pd.isna(v) else f"{v:.0%}"
        for _, r in cov.iterrows():
            lines.append(f"| {r['season']} | {r['league']} | {r['matches_with_result']} | {pct(r['share_pinnacle'])} | "
                         f"{pct(r['share_bet365'])} | {pct(r['share_max'])} | {pct(r['share_avg'])} | "
                         f"{'' if pd.isna(r['pinnacle_close_dates']) else r['pinnacle_close_dates']} | {r['last_date_in_file']} |")
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
