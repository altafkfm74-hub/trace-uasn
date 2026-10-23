"""
BOMT baseline.

    "Cooperative Highly-Maneuvering Target Tracking Using Multi-AUV
     Networks: A Bearing-Only Approach"
"""
from trace.sim.protocol import Protocol
import numpy as np


class BOMTProtocol(Protocol):
    name = "BOMT"

    def choose_forwarder(self, i_node, neighbours, params):
        best, best_s = None, -np.inf
        for j in neighbours:
            if j.xyz[2] >= i_node.xyz[2]:
                continue
            s = 0.4 * (i_node.xyz[2] - j.xyz[2]) - 0.3 * (1 - j.eta)
            if s > best_s:
                best_s = s
                best = {"id": j.idx, "z": j.xyz[2], "E": j.E, "q": j.q,
                        "E_Ntx": 1.5, "eta": j.eta, "_score": s}
        return best
