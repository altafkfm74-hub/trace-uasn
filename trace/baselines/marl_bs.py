"""
MARL-BS baseline (closest prior work).

    "Energy-Efficient, Multi-Agent Deep Reinforcement Learning Approach
     for Adaptive Beacon Selection in AUV-Based Underwater Localization"
"""
from trace.sim.protocol import Protocol
import numpy as np


class MARLBSProtocol(Protocol):
    name = "MARL-BS"

    def choose_forwarder(self, i_node, neighbours, params):
        best, best_s = None, -np.inf
        for j in neighbours:
            if j.xyz[2] >= i_node.xyz[2]:
                continue
            s = 0.5 * (i_node.xyz[2] - j.xyz[2]) - 0.5 * (1 - j.eta)
            if s > best_s:
                best_s = s
                best = {"id": j.idx, "z": j.xyz[2], "E": j.E, "q": j.q,
                        "E_Ntx": 1.5, "eta": j.eta, "_score": s}
        return best
