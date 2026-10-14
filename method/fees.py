"""Polymarket US costs, break-even, edge after costs, fractional Kelly.

Fee schedule (docs.polymarket.us/fees, effective 7 Oct 2026):
    taker fee per contract = coefficient * p * (1 - p)
with coefficient 0.0695 (0.10 for table tennis) and p the contract price in
dollars (0–1). Maximum $1.74 per 100 contracts at 50¢. Makers under $10M of
prior-month maker volume earn no rebate from 19 Oct 2026.

Combos add a 0.06(1-p)^4 term and carry no rebate; the method never buys them.
"""
from __future__ import annotations

TAKER_COEFFICIENT = 0.0695
TABLE_TENNIS_COEFFICIENT = 0.10


def taker_fee(price: float, coefficient: float = TAKER_COEFFICIENT) -> float:
    """Fee in dollars per contract for taking at `price` (0–1)."""
    _check(price)
    return coefficient * price * (1.0 - price)


def taker_fee_pct_of_stake(price: float, coefficient: float = TAKER_COEFFICIENT) -> float:
    """Fee as a fraction of the dollars staked (price per contract)."""
    return taker_fee(price, coefficient) / price


def taker_breakeven(price: float, coefficient: float = TAKER_COEFFICIENT) -> float:
    """Win probability needed to break even buying at `price` as a taker.

    EV per contract = p_win*(1-price) - (1-p_win)*price - fee = p_win - price - fee,
    so break-even is price + fee. At 50¢: 0.5174.
    """
    return price + taker_fee(price, coefficient)


def taker_edge(p_hat: float, ask: float, coefficient: float = TAKER_COEFFICIENT) -> float:
    """Expected profit per contract (in dollars) buying at the ask as a taker."""
    _check(ask)
    return p_hat - ask - taker_fee(ask, coefficient)


def maker_edge(p_hat: float, bid: float, rebate: float = 0.0) -> float:
    """Expected profit per contract resting a bid that gets filled.

    rebate is a positive dollar amount per contract if a tier pays one.
    """
    _check(bid)
    return p_hat - bid + rebate


def kelly_fraction(p_hat: float, price: float, fee: float = 0.0, fraction: float = 0.25) -> float:
    """Fraction of bankroll to stake on a binary contract bought at `price`.

    Win gains (1 - price - fee) per contract, loss costs (price + fee).
    Full Kelly f* = (p_hat*win - (1-p_hat)*lose) / win; we return fraction*f*.
    Benter: overestimating the edge 2x makes full Kelly negative-growth, so
    the method uses 1/4 Kelly at most and flat units before calibration is
    proven.
    """
    _check(price)
    win = 1.0 - price - fee
    lose = price + fee
    if win <= 0:
        return 0.0
    f_star = (p_hat * win - (1.0 - p_hat) * lose) / win
    return max(0.0, f_star) * fraction


def _check(price: float) -> None:
    if not (0.0 < price < 1.0):
        raise ValueError("price must be in (0, 1)")
