"""
QE-ORP baseline.

Implements the routing rule described in:

    "QoS-Aware and Energy-Optimized Cooperative Opportunistic Routing
     Protocol for Underwater Wireless Sensor Networks in Water Resource
     Management"

Weighted sum of depth, energy, and buffer with no normalization and no
confidence term, matching Section II-B critique.
"""
from trace.sim.protocol import Protocol
import numpy as np


class QEORPProtocol(Protocol):
    name = "QE-ORP"

    def choose_forwarder(self, i_node, neighbours, params):
        best, best_s = None, -np.inf
        for j in neighbours:
            if j.xyz[2] >= i_node.xyz[2]:
                continue
            dz = i_node.xyz[2] - j.xyz[2]
            s = 0.5 * dz - 0.5 * (1 - j.E / params["E_max"]) - 0.05 * j.q
            if s > best_s:
                best_s = s
                best = {"id": j.idx, "z": j.xyz[2], "E": j.E, "q": j.q,
                        "E_Ntx": 1.5, "eta": j.eta, "_score": s}
        return best
