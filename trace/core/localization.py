"""
ToA ranging and EKF localization — Eqs. (ranging) … (cov_update).
"""
from __future__ import annotations
import numpy as np


def toa_measurement(distance, c0, delta_c=0.0, noise_std=0.0, rng=None):
    """Eqs. (ranging), (sound_speed)."""
    t = distance / (c0 + delta_c)
    if noise_std > 0.0 and rng is not None:
        t += rng.normal(0.0, noise_std)
    return float(t)


def toa_taylor(distance, c0, delta_c=0.0):
    """Eq. (range_noisy)."""
    return float(distance / c0 - (distance / (c0 ** 2)) * delta_c)


def F_Q(dt, sigma_w2, dim=3):
    """Eq. (F_Q)."""
    I = np.eye(dim)
    F = np.block([[I, dt * I], [np.zeros((dim, dim)), I]])
    Q = sigma_w2 * np.block([[(dt ** 3) / 3.0 * I, (dt ** 2) / 2.0 * I],
                             [(dt ** 2) / 2.0 * I, dt * I]])
    return F, Q


def ekf_predict(state, cov, F, Q):
    """Eqs. (state_predict), (cov_predict)."""
    return F @ state, F @ cov @ F.T + Q


def kalman_gain(cov_pred, H, R):
    """Eq. (kalman_gain)."""
    S = H @ cov_pred @ H.T + R
    return np.linalg.solve(S, (cov_pred @ H.T).T).T


def ekf_update(state_pred, cov_pred, innovation, H, R):
    """Eqs. (state_update), (cov_update)."""
    K = kalman_gain(cov_pred, H, R)
    s = state_pred + K @ innovation
    I = np.eye(cov_pred.shape[0])
    P = (I - K @ H) @ cov_pred
    return s, 0.5 * (P + P.T)


def toa_jacobian(x_node, x_anchor, c0, dim=3):
    """Observation Jacobian H_k for ToA."""
    d = x_node - x_anchor
    r = max(np.linalg.norm(d), 1e-9)
    H = np.zeros((1, 2 * dim))
    H[0, :dim] = (d / r) / c0
    return H
