"""
ISAC-MAC baseline.

    "MAC Protocol for ISAC in Underwater Acoustic Networks with Dynamic
     Target Monitoring–Localization–Tracking"
"""
from trace.sim.protocol import Protocol


class ISACMACProtocol(Protocol):
    name = "ISAC-MAC"

    def choose_forwarder(self, i_node, neighbours, params):
        cands = [j for j in neighbours if j.xyz[2] < i_node.xyz[2]]
        if not cands:
            return None
        j = max(cands, key=lambda n: i_node.xyz[2] - n.xyz[2])
        return {"id": j.idx, "z": j.xyz[2], "E": j.E, "q": j.q,
                "E_Ntx": 1.5, "eta": j.eta, "_score": 0.0}
