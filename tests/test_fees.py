import pytest

from method.fees import (TABLE_TENNIS_COEFFICIENT, kelly_fraction, maker_edge,
                         taker_breakeven, taker_edge, taker_fee,
                         taker_fee_pct_of_stake)


def test_fee_at_fifty_cents_is_1_74_cents():
    assert taker_fee(0.5) == pytest.approx(0.017375)
    assert taker_fee(0.5) * 100 == pytest.approx(1.7375)   # $1.74 per 100 contracts


def test_fee_share_of_stake_matches_doc():
    assert taker_fee_pct_of_stake(0.5) == pytest.approx(0.03475, abs=1e-4)   # 3.5%
    assert taker_fee_pct_of_stake(0.2) == pytest.approx(0.0556, abs=1e-3)    # 5.6%
    assert taker_fee_pct_of_stake(0.8) == pytest.approx(0.0139, abs=1e-3)    # 1.4%
    assert taker_fee_pct_of_stake(0.1) == pytest.approx(0.0626, abs=1e-3)    # 6.3%


def test_breakeven_at_fifty_cents():
    assert taker_breakeven(0.5) == pytest.approx(0.5174, abs=1e-4)


def test_table_tennis_coefficient_is_higher():
    assert taker_fee(0.5, TABLE_TENNIS_COEFFICIENT) > taker_fee(0.5)


def test_edges():
    # Our price 0.55, ask 0.52: 3 points minus a 1.73c fee ≈ 1.27c per contract
    assert taker_edge(0.55, 0.52) == pytest.approx(0.55 - 0.52 - 0.0695 * 0.52 * 0.48)
    assert maker_edge(0.55, 0.52) == pytest.approx(0.03)
    assert taker_edge(0.50, 0.50) < 0            # fair price, fee makes it negative
    assert maker_edge(0.50, 0.50) == 0.0


def test_kelly():
    # p=0.55 at 0.50 with no fee: f* = (0.55-0.5)/(0.5) = 0.10; quarter Kelly 0.025
    assert kelly_fraction(0.55, 0.5, fee=0.0, fraction=1.0) == pytest.approx(0.10)
    assert kelly_fraction(0.55, 0.5, fee=0.0, fraction=0.25) == pytest.approx(0.025)
    assert kelly_fraction(0.50, 0.5, fee=0.017375) == 0.0      # no edge → no bet
    assert kelly_fraction(0.55, 0.5, fee=0.017375, fraction=0.25) < 0.025


def test_price_validation():
    with pytest.raises(ValueError):
        taker_fee(1.0)
    with pytest.raises(ValueError):
        maker_edge(0.5, 0.0)
