"""
ARQ loop.
"""
from __future__ import annotations
import numpy as np
from trace.core.link_model import expected_transmissions


def transmit(per: float, rng: np.random.Generator, max_tx: int = 5):
    """Return (delivered, n_tx_used)."""
    for k in range(1, max_tx + 1):
        if rng.random() > per:
            return True, k
    return False, max_tx


def expected_n_tx(per: float) -> float:
    return expected_transmissions(per)
