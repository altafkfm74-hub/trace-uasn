"""
Link quality, PER, and energy — Eqs. (rx_power) … (energy_per_packet).
"""
from __future__ import annotations


def path_gain(distance, frequency_khz, absorption_db_per_khz=0.0):
    """G(d, f) in Eq. (rx_power)."""
    if distance <= 0.0:
        raise ValueError("distance must be positive")
    spreading = 1.0 / (distance ** 2)
    A = absorption_db_per_khz * frequency_khz
    return float(spreading * 10.0 ** (-A * distance / 10.0))


def rx_power(P_tx, distance, frequency_khz, absorption_db_per_khz=0.0):
    """Eq. (rx_power)."""
    return float(P_tx * path_gain(distance, frequency_khz, absorption_db_per_khz))


def sinr(P_rx, N0, bandwidth_hz, interference_w=0.0):
    """Eq. (sinr)."""
    return float(P_rx / max(N0 * bandwidth_hz + interference_w, 1e-30))


def per_from_ack(n_success, n_tx, eps=1e-9):
    """Eq. (per_ack)."""
    if n_tx <= 0:
        return 0.0
    p = 1.0 - n_success / max(n_tx, eps)
    return float(min(max(p, 0.0), 1.0))


def expected_transmissions(p_err, cap=1e6):
    """Eq. (expected_tx)."""
    p = min(max(float(p_err), 0.0), 1.0 - 1e-12)
    return float(min(1.0 / (1.0 - p), cap))


def energy_per_packet(E_Ntx, P_tx, T_pkt, E_c):
    """Eq. (energy_per_packet)."""
    return float(E_Ntx * (P_tx * T_pkt + E_c))
