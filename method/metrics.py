"""Scorecard math: log loss, Brier, calibration, Murphy decomposition, CLV.

All probabilities are for the event that y == 1. Arrays are numpy-compatible.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import numpy as np

EPS = 1e-12


def _pair(p: Iterable[float], y: Iterable[float]):
    p = np.clip(np.asarray(list(p), dtype=float), EPS, 1 - EPS)
    y = np.asarray(list(y), dtype=float)
    if p.shape != y.shape:
        raise ValueError("p and y must have the same length")
    return p, y


def log_loss(p, y) -> float:
    p, y = _pair(p, y)
    return float(-np.mean(y * np.log(p) + (1 - y) * np.log(1 - p)))


def brier(p, y) -> float:
    p, y = _pair(p, y)
    return float(np.mean((p - y) ** 2))


def logit(p):
    p = np.clip(np.asarray(p, dtype=float), EPS, 1 - EPS)
    return np.log(p / (1 - p))


def expit(x):
    return 1.0 / (1.0 + np.exp(-np.asarray(x, dtype=float)))


@dataclass
class CalibrationFit:
    intercept: float
    slope: float
    intercept_se: float
    slope_se: float
    n: int

    @property
    def slope_ci95(self) -> tuple[float, float]:
        return (self.slope - 1.96 * self.slope_se, self.slope + 1.96 * self.slope_se)


def calibration_fit(p, y, iters: int = 50) -> CalibrationFit:
    """Logistic recalibration y ~ a + b*logit(p).

    A perfectly calibrated forecaster has a = 0, b = 1. b < 1 means the
    forecasts are over-confident (too extreme); b > 1 under-confident.
    Newton–Raphson with standard errors from the inverse Hessian.
    """
    p, y = _pair(p, y)
    x = logit(p)
    X = np.column_stack([np.ones_like(x), x])
    beta = np.array([0.0, 1.0])
    for _ in range(iters):
        mu = expit(X @ beta)
        W = mu * (1 - mu)
        grad = X.T @ (y - mu)
        H = (X * W[:, None]).T @ X
        try:
            step = np.linalg.solve(H, grad)
        except np.linalg.LinAlgError:
            break
        beta = beta + step
        if np.max(np.abs(step)) < 1e-10:
            break
    mu = expit(X @ beta)
    W = mu * (1 - mu)
    H = (X * W[:, None]).T @ X
    cov = np.linalg.pinv(H)
    se = np.sqrt(np.maximum(np.diag(cov), 0.0))
    return CalibrationFit(float(beta[0]), float(beta[1]), float(se[0]), float(se[1]), int(y.size))


@dataclass
class Murphy:
    brier: float
    reliability: float
    resolution: float
    uncertainty: float
    bins: int

    def check(self) -> float:
        """Brier - (reliability - resolution + uncertainty); ~0 if consistent."""
        return self.brier - (self.reliability - self.resolution + self.uncertainty)


def murphy_decomposition(p, y, bins: int = 10) -> Murphy:
    """Brier = reliability - resolution + uncertainty, on equal-width bins.

    Reliability (lower is better) is miscalibration; resolution (higher is
    better) is how much the forecasts separate outcomes; uncertainty is the
    base-rate variance you cannot change.
    """
    p, y = _pair(p, y)
    edges = np.linspace(0, 1, bins + 1)
    idx = np.clip(np.digitize(p, edges[1:-1]), 0, bins - 1)
    ybar = y.mean()
    rel = res = 0.0
    for b in range(bins):
        m = idx == b
        if not m.any():
            continue
        nk = m.sum()
        pk = p[m].mean()
        ok = y[m].mean()
        rel += nk * (pk - ok) ** 2
        res += nk * (ok - ybar) ** 2
    n = y.size
    return Murphy(brier(p, y), rel / n, res / n, ybar * (1 - ybar), bins)


def calibration_table(p, y, bins: int = 10):
    """Per-bin mean forecast, observed frequency and count (as dicts)."""
    p, y = _pair(p, y)
    edges = np.linspace(0, 1, bins + 1)
    idx = np.clip(np.digitize(p, edges[1:-1]), 0, bins - 1)
    rows = []
    for b in range(bins):
        m = idx == b
        if not m.any():
            continue
        rows.append({
            "bin_lo": float(edges[b]),
            "bin_hi": float(edges[b + 1]),
            "n": int(m.sum()),
            "mean_forecast": float(p[m].mean()),
            "observed": float(y[m].mean()),
        })
    return rows


# --- Closing-line value -----------------------------------------------------

def clv_points(entry_price: float, closing_mid: float, side: str = "long") -> float:
    """CLV in probability points on a binary contract.

    long  = we hold Yes bought at entry_price; closing_mid is the last
            pre-game Yes mid. Positive when the market moved our way.
    short = we hold No (or sold Yes) at entry_price (the Yes price we sold at).
    """
    if side == "long":
        return float(closing_mid - entry_price)
    if side == "short":
        return float(entry_price - closing_mid)
    raise ValueError("side must be 'long' or 'short'")


def clv_percent(entry_price: float, closing_mid: float, side: str = "long") -> float:
    """CLV as a percentage of the entry price (price-relative form)."""
    pts = clv_points(entry_price, closing_mid, side)
    return float(pts / entry_price)


def clv_odds(odds_taken: float, fair_closing_prob: float) -> float:
    """Sportsbook form: odds_taken * fair_closing_prob - 1 (Buchdahl/Pinnacle).

    0.03 means the price we took was 3% better than the fair closing price.
    """
    return float(odds_taken * fair_closing_prob - 1.0)


# --- Sample sizes -----------------------------------------------------------

def bets_to_separate(win_rate: float, hurdle: float, z: float = 2.0) -> int:
    """Bets needed for win_rate to sit z standard errors above hurdle.

    bets_to_separate(0.55, 0.5238) ≈ 1,460; bets_to_separate(0.55, 0.5174) ≈ 930.
    """
    if win_rate <= hurdle:
        raise ValueError("win_rate must exceed hurdle")
    sd = np.sqrt(win_rate * (1 - win_rate))
    return int(np.ceil((z * sd / (win_rate - hurdle)) ** 2))


def bets_to_detect_clv(mean_clv_pts: float, sd_clv_pts: float, z: float = 2.0) -> int:
    """Bets needed for a mean CLV (in points) to be z standard errors from zero.

    sd_clv_pts must be measured from our own log (the doc assumes 3–4 points).
    """
    if mean_clv_pts <= 0 or sd_clv_pts <= 0:
        raise ValueError("mean and sd must be positive")
    return int(np.ceil((z * sd_clv_pts / mean_clv_pts) ** 2))


def expected_longest_losing_streak(n: int, win_rate: float) -> float:
    """Rough expectation of the longest losing run in n bets (log base 1/q)."""
    q = 1 - win_rate
    return float(np.log(n * win_rate) / np.log(1 / q))
