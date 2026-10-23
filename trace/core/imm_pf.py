"""
IMM-PF tracking filter — Eqs. (imm_motion) … (tracking_quality).
"""
from __future__ import annotations
from typing import Tuple
import numpy as np
from numpy.typing import ArrayLike


def transition_cv(dt: float) -> np.ndarray:
    """F_CV in Eq. (imm_models)."""
    return np.array([[1.0, dt, 0.0, 0.0],
                     [0.0, 1.0, 0.0, 0.0],
                     [0.0, 0.0, 1.0, dt],
                     [0.0, 0.0, 0.0, 1.0]], dtype=float)


def transition_ct(dt: float, omega: float) -> np.ndarray:
    """F_CT in Eq. (imm_models)."""
    if abs(omega) < 1e-9:
        return transition_cv(dt)
    s, c = np.sin(omega * dt), np.cos(omega * dt)
    return np.array([[1.0, s / omega, 0.0, (c - 1.0) / omega],
                     [0.0, c, 0.0, s],
                     [0.0, (1.0 - c) / omega, 0.0, s / omega],
                     [0.0, s, 0.0, c]], dtype=float)


def interaction(means, covs, mu, Pi):
    """IMM input interaction (step 1 of the cycle)."""
    n = mu.size
    cbar = Pi.T @ mu
    cbar = np.maximum(cbar, 1e-300)
    x0, P0 = [], []
    for j in range(n):
        w_ij = (Pi[:, j] * mu) / cbar[j]
        m0 = sum(w_ij[i] * means[i] for i in range(n))
        P = np.zeros_like(covs[0])
        for i in range(n):
            d = means[i] - m0
            P += w_ij[i] * (covs[i] + np.outer(d, d))
        x0.append(m0); P0.append(P)
    return x0, P0, cbar


def model_probability(likelihoods, cbar, Pi):
    """Eq. (model_prob)."""
    L = np.asarray(likelihoods, dtype=float)
    num = L * cbar
    den = num.sum()
    if den <= 0.0 or not np.isfinite(den):
        return np.full_like(L, 1.0 / L.size)
    return num / den


def combine(means, covs, mu):
    """Eq. (imm_combine)."""
    x = sum(mu[j] * means[j] for j in range(mu.size))
    P = np.zeros_like(covs[0])
    for j in range(mu.size):
        d = means[j] - x
        P += mu[j] * (covs[j] + np.outer(d, d))
    return x, P


def pf_weight(prev_w, p_meas, p_trans, q_prop):
    """Eq. (pf_weight)."""
    w = prev_w * p_meas * p_trans / np.maximum(q_prop, 1e-300)
    s = w.sum()
    return np.full_like(w, 1.0 / w.size) if s <= 0 or not np.isfinite(s) else w / s


def pf_estimate(particles, weights):
    """Eq. (pf_est)."""
    x_hat = weights @ particles
    d = particles - x_hat
    return x_hat, (weights[:, None] * d).T @ d


def resample(particles, weights, rng, ess_threshold=None):
    """Systematic resampling if ESS < N/2."""
    n = weights.size
    thr = ess_threshold if ess_threshold is not None else n / 2.0
    if 1.0 / np.sum(weights ** 2) >= thr:
        return particles, weights
    positions = (rng.random() + np.arange(n)) / n
    cum = np.cumsum(weights); cum[-1] = 1.0
    idx = np.searchsorted(cum, positions)
    return particles[idx], np.full(n, 1.0 / n)


def nis_residual(z, h, S):
    """Eq. (tracking_residual)."""
    e = z - h
    return float(e @ np.linalg.solve(S, e))


def quality_from_nis(r):
    """Eq. (tracking_quality)."""
    return float(np.exp(-r / 2.0))
