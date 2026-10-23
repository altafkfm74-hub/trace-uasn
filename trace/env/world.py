"""
World container and default deployment.
"""
from __future__ import annotations
from dataclasses import dataclass, field
import numpy as np


@dataclass
class World:
    region_xyz: tuple = (1000.0, 1000.0, 500.0)
    n_nodes: int = 50
    seed: int = 0
    sink_xyz: tuple = None
    node_positions: np.ndarray = None
    auvs: list = field(default_factory=list)


def default_world(seed: int = 0, n_nodes: int = 50) -> World:
    rng = np.random.default_rng(seed)
    W, H, D = 1000.0, 1000.0, 500.0
    pos = np.column_stack([
        rng.uniform(0, W, n_nodes),
        rng.uniform(0, H, n_nodes),
        rng.uniform(50, D - 50, n_nodes),
    ])
    return World(region_xyz=(W, H, D), n_nodes=n_nodes, seed=seed,
                 sink_xyz=(W / 2, H / 2, 0.0), node_positions=pos)
