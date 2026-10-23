import numpy as np
from trace.core import imm_pf


def test_transition_shapes():
    F1 = imm_pf.transition_cv(0.5)
    F2 = imm_pf.transition_ct(0.5, 0.1)
    assert F1.shape == (4, 4)
    assert F2.shape == (4, 4)


def test_quality_bounds():
    r = imm_pf.nis_residual(np.array([1.0, 0.0]), np.zeros(2), np.eye(2))
    q = imm_pf.quality_from_nis(r)
    assert 0.0 < q <= 1.0
