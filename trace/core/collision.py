"""
Multi-AUV coordination — Eqs. (collision_condition) … (multi_auv_fusion).
"""
from __future__ import annotations
import numpy as np

DELTA_Z_MIN, R_SAFE, DT_SLOT, DELTA_GUARD, R_BEACON = 50.0, 50.0, 2.0, 0.5, 300.0


def collision_condition(z_m, z_n, x_m, x_n, dz_min=DELTA_Z_MIN, R_safe=R_SAFE):
    """Eq. (collision_condition)."""
    if abs(z_m - z_n) >= dz_min:
        return True
    dx = np.asarray(x_m, float) - np.asarray(x_n, float)
    return bool(np.linalg.norm(dx) >= R_safe)


def beacon_slot(t0, m_index, dt_slot=DT_SLOT):
    """Eq. (beacon_schedule)."""
    return float(t0 + m_index * dt_slot)


def interference_free(t_m, t_n, d_max, c0, delta_guard=DELTA_GUARD):
    """Eq. (interference_free)."""
    return bool(abs(t_m - t_n) >= d_max / c0 + delta_guard)


def proximity(x_m, x_n, R_safe=R_SAFE):
    """Eq. (proximity)."""
    return bool(np.linalg.norm(np.asarray(x_m, float) - np.asarray(x_n, float)) < R_safe)


def collision_probability_bound(lambda_enc, P_fail, T):
    """Eq. (collision_prob)."""
    return float(1.0 - np.exp(-lambda_enc * P_fail * T))


def measurement_set(x_i, auv_positions, R_beacon=R_BEACON):
    """Eq. (measurement_set)."""
    p = np.asarray(x_i, float)
    return [m for m, xa in enumerate(auv_positions)
            if np.linalg.norm(p - np.asarray(xa, float)) <= R_beacon]


def multi_auv_fusion(state_pred, K, innovations):
    """Eq. (multi_auv_fusion)."""
    total = np.zeros_like(state_pred)
    for e in innovations:
        total += e
    return state_pred + K @ total
