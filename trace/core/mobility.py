"""
Node mobility — Eq. (mobility); re-exports F_Q.
"""
from __future__ import annotations
import numpy as np
from trace.core.localization import F_Q as _F_Q


def drift_step(x, v, dt, rng=None, sigma_w2=0.0):
    """Eq. (mobility)."""
    x_new = x + v * dt
    if rng is not None and sigma_w2 > 0.0:
        x_new = x_new + rng.normal(0.0, np.sqrt(sigma_w2 * dt), size=x.shape)
    return x_new


def F_Q(dt, sigma_w2, dim=3):
    """Alias of localization.F_Q."""
    return _F_Q(dt, sigma_w2, dim)
