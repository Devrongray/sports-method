"""De-vigging: turn a set of prices into probabilities that sum to one.

Input is decimal odds (one per outcome). q_i = 1/odds_i are the implied
probabilities; their sum minus one is the overround.

Methods (Štrumbelj 2014; Clarke, Kovalchik & Ingram 2017):

- multiplicative: p_i = q_i / sum(q)          (basic normalisation)
- additive:       p_i = q_i - (sum(q) - 1)/n  (equal margin per outcome)
- power:          p_i = q_i ** k, k solved so sum(p) = 1
- shin:           Shin (1993) insider model, z solved so sum(p) = 1.
                  For two outcomes it is identical to additive (Clarke et al.).

Shin's z is best read as a measure of favourite-longshot curvature, not as a
literal insider share (Run 2: the tote placebo returned the same z).
"""
from __future__ import annotations

from typing import Iterable, Sequence

import numpy as np

METHODS = ("multiplicative", "additive", "power", "shin")


def implied(odds: Iterable[float]) -> np.ndarray:
    """Overrounded implied probabilities 1/odds."""
    o = np.asarray(list(odds), dtype=float)
    if o.ndim != 1 or o.size < 2:
        raise ValueError("need at least two decimal odds")
    if np.any(o <= 1.0):
        raise ValueError("decimal odds must be > 1")
    return 1.0 / o


def overround(odds: Iterable[float]) -> float:
    """sum(1/odds) - 1; the bookmaker's margin before any de-vig."""
    return float(implied(odds).sum() - 1.0)


def multiplicative(odds: Iterable[float]) -> np.ndarray:
    q = implied(odds)
    return q / q.sum()


def additive(odds: Iterable[float]) -> np.ndarray:
    q = implied(odds)
    p = q - (q.sum() - 1.0) / q.size
    if np.any(p <= 0):
        # Can happen on long-priced outcomes in large fields; fall back to
        # multiplicative rather than return a negative probability.
        return multiplicative(odds)
    return p


def _bisect(f, lo: float, hi: float, tol: float = 1e-12, iters: int = 200) -> float:
    """Root of a decreasing function f on [lo, hi]: f(lo) > 0 > f(hi)."""
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        if f(mid) > 0:
            lo = mid
        else:
            hi = mid
        if hi - lo < tol:
            break
    return 0.5 * (lo + hi)


def power(odds: Iterable[float]) -> np.ndarray:
    q = implied(odds)
    hi = 1.0
    while (q ** hi).sum() > 1.0:
        hi *= 2.0
        if hi > 1e6:
            raise ValueError("power method did not converge")
    k = _bisect(lambda k: (q ** k).sum() - 1.0, 1.0, hi)
    p = q ** k
    return p / p.sum()


def shin_z(odds: Iterable[float]) -> float:
    """Shin's z for a market with 3+ outcomes (0 for two-way markets)."""
    q = implied(odds)
    if q.size == 2:
        return 0.0
    s = q.sum()

    def probs(z: float) -> np.ndarray:
        return (np.sqrt(z * z + 4.0 * (1.0 - z) * q * q / s) - z) / (2.0 * (1.0 - z))

    return _bisect(lambda z: probs(z).sum() - 1.0, 0.0, 1.0 - 1e-9)


def shin(odds: Iterable[float]) -> np.ndarray:
    q = implied(odds)
    if q.size == 2:
        return additive(odds)
    s = q.sum()
    z = shin_z(odds)
    p = (np.sqrt(z * z + 4.0 * (1.0 - z) * q * q / s) - z) / (2.0 * (1.0 - z))
    return p / p.sum()


def devig(odds: Sequence[float], method: str = "shin") -> np.ndarray:
    """Dispatch by method name."""
    if method == "multiplicative":
        return multiplicative(odds)
    if method == "additive":
        return additive(odds)
    if method == "power":
        return power(odds)
    if method == "shin":
        return shin(odds)
    raise ValueError(f"unknown method {method!r}; choose from {METHODS}")


def fair_from_american(american: Sequence[float], method: str = "shin") -> np.ndarray:
    """Convenience: American odds (e.g. -110, +150) to fair probabilities."""
    dec = [1.0 + 100.0 / abs(a) if a < 0 else 1.0 + a / 100.0 for a in american]
    return devig(dec, method)


def fair_from_yes_no_prices(yes_ask: float, no_ask: float, method: str = "additive") -> float:
    """Fair Yes probability from a binary contract's two asks (prices in 0–1).

    yes_ask + no_ask > 1 by the spread; de-vig the pair like a two-way book.
    """
    if not (0 < yes_ask < 1 and 0 < no_ask < 1):
        raise ValueError("prices must be in (0, 1)")
    p = devig([1.0 / yes_ask, 1.0 / no_ask], method)
    return float(p[0])
