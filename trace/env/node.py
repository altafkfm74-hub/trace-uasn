"""
Sensor node state.
"""
from __future__ import annotations
from dataclasses import dataclass
import numpy as np


@dataclass
class Node:
    idx: int
    xyz: np.ndarray
    E0: float = 1000.0
    Q_max: int = 50
    E: float = None
    q: int = 0
    eta: float = 0.5
    velocity: np.ndarray = None

    def __post_init__(self):
        if self.E is None:
            self.E = self.E0
        if self.velocity is None:
            self.velocity = np.zeros(3)


def make_nodes(positions: np.ndarray) -> list:
    return [Node(idx=i, xyz=np.asarray(p, float)) for i, p in enumerate(positions)]
