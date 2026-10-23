"""
Metrics container.
"""
from __future__ import annotations
from dataclasses import dataclass, field
import numpy as np


@dataclass
class Metrics:
    delivered: int = 0
    sent: int = 0
    delays_s: list = field(default_factory=list)
    per_delivery_energy_j: list = field(default_factory=list)
    energy_used_j: list = field(default_factory=list)
    death_times_h: list = field(default_factory=list)
    per_source_last_t: dict = field(default_factory=dict)
    per_source_aoi_s: list = field(default_factory=list)

    @property
    def pdr(self) -> float:
        return float(self.delivered / self.sent) if self.sent else 0.0

    @property
    def mean_delay_s(self) -> float:
        return float(np.mean(self.delays_s)) if self.delays_s else 0.0

    @property
    def energy_per_bit_nj(self) -> float:
        if not self.per_delivery_energy_j:
            return 0.0
        return float(np.mean(self.per_delivery_energy_j) * 1e9)

    @property
    def fnd_h(self) -> float:
        return float(min(self.death_times_h)) if self.death_times_h else float("inf")

    @property
    def lnd_h(self) -> float:
        return float(max(self.death_times_h)) if self.death_times_h else float("inf")
