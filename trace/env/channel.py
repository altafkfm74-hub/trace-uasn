"""
Acoustic channel: SNR-to-PER mapping.
"""
from __future__ import annotations
import numpy as np
from trace.core.link_model import rx_power, sinr


def per_from_sinr(sinr_db: float, p_floor: float = 0.02, slope: float = 1.2) -> float:
    p = p_floor + (1.0 - p_floor) / (1.0 + np.exp((sinr_db - 10.0) / slope))
    return float(np.clip(p, 0.0, 1.0))


def link_per(x_tx, x_rx, P_tx=2.0, f_khz=18.0,
             N0=1e-15, B=10_000.0, I_w=0.0) -> float:
    d = float(np.linalg.norm(np.asarray(x_tx, float) - np.asarray(x_rx, float)))
    pr = rx_power(P_tx, d, f_khz)
    sn = sinr(pr, N0, B, I_w)
    snr_db = 10.0 * np.log10(max(sn, 1e-30))
    return per_from_sinr(snr_db)
