import numpy as np
import pytest

from method.metrics import (bets_to_detect_clv, bets_to_separate, brier,
                            calibration_fit, calibration_table, clv_odds,
                            clv_percent, clv_points,
                            expected_longest_losing_streak, log_loss,
                            murphy_decomposition)


def _synthetic(n=20000, slope=1.0, intercept=0.0, seed=0):
    rng = np.random.default_rng(seed)
    p = rng.uniform(0.05, 0.95, n)
    x = np.log(p / (1 - p))
    q = 1 / (1 + np.exp(-(intercept + slope * x)))
    y = (rng.uniform(size=n) < q).astype(float)
    return p, y


def test_log_loss_and_brier_basic():
    assert log_loss([0.5, 0.5], [1, 0]) == pytest.approx(np.log(2))
    assert brier([0.5, 0.5], [1, 0]) == pytest.approx(0.25)
    assert log_loss([1.0], [1]) < 1e-9


def test_calibration_recovers_slope_one():
    p, y = _synthetic(slope=1.0)
    fit = calibration_fit(p, y)
    assert abs(fit.slope - 1.0) < 3 * fit.slope_se + 0.02
    assert abs(fit.intercept) < 0.08


def test_calibration_detects_overconfidence():
    p, y = _synthetic(slope=0.7)
    fit = calibration_fit(p, y)
    assert fit.slope < 0.8
    lo, hi = fit.slope_ci95
    assert lo < 0.7 < hi + 0.05


def test_murphy_identity():
    p, y = _synthetic()
    m = murphy_decomposition(p, y, bins=10)
    assert abs(m.check()) < 2e-3
    assert m.uncertainty == pytest.approx(y.mean() * (1 - y.mean()))
    assert m.resolution > 0


def test_calibration_table_rows():
    p, y = _synthetic(n=2000)
    rows = calibration_table(p, y, bins=5)
    assert sum(r["n"] for r in rows) == 2000
    for r in rows:
        assert r["bin_lo"] <= r["mean_forecast"] <= r["bin_hi"]


def test_clv_forms():
    assert clv_points(0.55, 0.58, "long") == pytest.approx(0.03)
    assert clv_points(0.55, 0.58, "short") == pytest.approx(-0.03)
    assert clv_percent(0.50, 0.52) == pytest.approx(0.04)
    assert clv_odds(2.10, 0.50) == pytest.approx(0.05)
    with pytest.raises(ValueError):
        clv_points(0.5, 0.5, "sideways")


def test_sample_sizes_match_the_doc():
    assert 1400 <= bets_to_separate(0.55, 0.5238) <= 1500   # ≈1,460
    assert 900 <= bets_to_separate(0.55, 0.5174) <= 960     # ≈930
    assert bets_to_detect_clv(2.0, 3.5) == 13               # (2*3.5/2)^2 = 12.25 → 13
    with pytest.raises(ValueError):
        bets_to_separate(0.50, 0.5238)


def test_losing_streak_rough():
    s = expected_longest_losing_streak(1000, 0.55)
    assert 7 < s < 9
