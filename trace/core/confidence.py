"""
Tracking-regulated confidence — Eqs. (normalized_cov), (confidence_loc), (confidence).
"""
from __future__ import annotations
import numpy as np


def normalize_cov(P, dt, dim=3, eps=1e-12):
    """Eq. (normalized_cov)."""
    I = np.eye(dim)
    J = np.block([[I, np.zeros((dim, dim))],
                  [np.zeros((dim, dim)), np.sqrt(max(dt, eps)) * I]])
    return J @ P @ J


def eta_loc(P_norm, eps=1e-9):
    """Eq. (confidence_loc)."""
    return float(1.0 / (np.trace(P_norm) + eps))


def eta(eta_loc_value, q_k):
    """Eq. (confidence)."""
    return float(eta_loc_value * q_k)
