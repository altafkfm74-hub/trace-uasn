"""
Protocol interface and TRACE reference protocol.
"""
from __future__ import annotations
import numpy as np
from trace.core import forwarder, confidence


class Protocol:
    name = "base"

    def update_eta(self, node, eta_loc_value: float, q_k: float) -> None:
        node.eta = confidence.eta(eta_loc_value, q_k)

    def choose_forwarder(self, i_node, neighbours, params):
        cands = [
            {"id": j.idx, "z": j.xyz[2], "E": j.E, "q": j.q,
             "E_Ntx": 1.5, "eta": j.eta}
            for j in neighbours
        ]
        return forwarder.select_forwarder(
            cands, z_i=i_node.xyz[2],
            dz_max=params["dz_max"], N_tx_max=params["N_tx_max"],
            E_max=params["E_max"], Q_max=params["Q_max"],
            eta_th=params["eta_th"],
            weights=params["weights"],
        )


class TRACEProtocol(Protocol):
    name = "TRACE"

    def choose_forwarder(self, i_node, neighbours, params):
        return super().choose_forwarder(i_node, neighbours, params)
