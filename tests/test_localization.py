import numpy as np
from trace.core import localization


def test_toa():
    t = localization.toa_measurement(1500.0, 1500.0, 10.0)
    assert abs(t - 1500.0 / 1510.0) < 1e-9


def test_ekf_dims():
    F, Q = localization.F_Q(0.5, 1e-3, dim=3)
    s, P = localization.ekf_predict(np.zeros(6), np.eye(6), F, Q)
    K = localization.kalman_gain(P, np.eye(1, 6), np.eye(1))
    assert K.shape == (6, 1)
