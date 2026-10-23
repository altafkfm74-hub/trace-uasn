import numpy as np
from trace.core import confidence


def test_eta_bounds():
    P = confidence.normalize_cov(np.eye(6), dt=0.5, dim=3)
    el = confidence.eta_loc(P)
    e = confidence.eta(el, 0.9)
    assert 0.0 < e <= 1.0
