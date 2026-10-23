"""
Forwarder score and selection — Eqs. (depth_progress) … (energy_update).
"""
from __future__ import annotations
from typing import Sequence
import numpy as np

DEFAULT_WEIGHTS = (0.35, 0.25, 0.15, 0.15, 0.10)
DEFAULT_ETA_TH  = 0.40


def depth_progress(z_i, z_j):
    """Eq. (depth_progress)."""
    return float(z_i - z_j)


def normalize_energy(E_j, E_max):
    """First half of Eq. (norm_energy)."""
    return 0.0 if E_max <= 0 else float(min(max(E_j / E_max, 0.0), 1.0))


def normalize_buffer(q_j, Q_max):
    """Second half of Eq. (norm_energy)."""
    return 0.0 if Q_max <= 0 else float(min(max(q_j / Q_max, 0.0), 1.0))


def score(dz_norm, E_Ntx_norm, E_bar_j, q_bar_j, eta_j,
          weights: Sequence[float] = DEFAULT_WEIGHTS):
    """Eq. (score)."""
    w_p, w_r, w_e, w_b, w_c = weights
    return float(w_p * dz_norm - w_r * E_Ntx_norm
                 - w_e * (1.0 - E_bar_j) - w_b * q_bar_j
                 - w_c * (1.0 - eta_j))


def is_eligible(z_i, z_j, eta_j, eta_th=DEFAULT_ETA_TH):
    """Candidate-set eligibility (depth + gate)."""
    return bool(z_j < z_i and eta_j >= eta_th)


def select_forwarder(candidates, z_i, dz_max, N_tx_max, E_max, Q_max,
                     eta_th=DEFAULT_ETA_TH, weights=DEFAULT_WEIGHTS):
    """Eq. (forwarder_select)."""
    best, best_s = None, -np.inf
    for c in candidates:
        if not is_eligible(z_i, c["z"], c["eta"], eta_th):
            continue
        dz_norm = float(np.clip(depth_progress(z_i, c["z"]) / dz_max, 0.0, 1.0))
        eN = float(np.clip(c["E_Ntx"] / N_tx_max, 0.0, 1.0))
        s = score(dz_norm, eN,
                  normalize_energy(c["E"], E_max),
                  normalize_buffer(c["q"], Q_max),
                  c["eta"], weights)
        if s > best_s:
            best_s, best = s, dict(c)
            best["_score"] = s
    return best


def update_energy(E_i, E_consumed):
    """First half of Eq. (energy_update)."""
    return float(max(E_i - E_consumed, 0.0))


def update_buffer(q_i, arrivals, service, Q_max):
    """Second half of Eq. (energy_update)."""
    return float(min(max(q_i + arrivals - service, 0.0), Q_max))
