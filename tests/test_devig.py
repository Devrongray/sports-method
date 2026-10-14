import numpy as np
import pytest

from method.devig import (METHODS, additive, devig, fair_from_american,
                          fair_from_yes_no_prices, multiplicative, overround,
                          power, shin, shin_z)

TWO_WAY = [1.909, 1.909]          # -110 / -110
THREE_WAY = [2.10, 3.40, 3.60]    # typical soccer 1X2 at a sharp book
FIELD = [1.5, 4.0, 9.0, 15.0, 30.0, 60.0]


@pytest.mark.parametrize("method", METHODS)
@pytest.mark.parametrize("odds", [TWO_WAY, THREE_WAY, FIELD])
def test_sums_to_one_and_positive(method, odds):
    p = devig(odds, method)
    assert p.shape == (len(odds),)
    assert np.all(p > 0)
    assert abs(p.sum() - 1.0) < 1e-9


def test_overround():
    assert abs(overround(TWO_WAY) - (2 / 1.909 - 1)) < 1e-12
    assert overround([2.0, 2.0]) == pytest.approx(0.0)


def test_two_way_even_money():
    for m in METHODS:
        assert devig(TWO_WAY, m) == pytest.approx([0.5, 0.5])


def test_shin_equals_additive_for_two_outcomes():
    odds = [1.40, 3.20]
    assert shin(odds) == pytest.approx(additive(odds))
    assert shin_z(odds) == 0.0


def test_ordering_preserved():
    for m in METHODS:
        p = devig(FIELD, m)
        assert np.all(np.diff(p) < 0)


def test_power_and_shin_shrink_longshots_more_than_multiplicative():
    # Both methods assign the longshot a smaller share of the overround
    # removal than the favourite, so the longshot ends up *below* its
    # multiplicative probability and the favourite above it.
    mult, pw, sh = multiplicative(FIELD), power(FIELD), shin(FIELD)
    assert pw[-1] < mult[-1] and sh[-1] < mult[-1]
    assert pw[0] > mult[0] and sh[0] > mult[0]


def test_shin_z_reasonable_on_three_way():
    z = shin_z(THREE_WAY)
    assert 0.0 < z < 0.1


def test_american():
    p = fair_from_american([-110, -110])
    assert p == pytest.approx([0.5, 0.5])
    p = fair_from_american([-200, +170], "multiplicative")
    assert p[0] > p[1] and abs(p.sum() - 1) < 1e-9


def test_yes_no_prices():
    # Yes ask 0.57, No ask 0.45 → overround 2%; fair Yes near 0.56
    f = fair_from_yes_no_prices(0.57, 0.45)
    assert 0.55 < f < 0.57
    with pytest.raises(ValueError):
        fair_from_yes_no_prices(1.2, 0.3)


def test_bad_inputs():
    with pytest.raises(ValueError):
        devig([1.0, 2.0], "shin")
    with pytest.raises(ValueError):
        devig([2.0, 2.0], "nope")
