"""
Event-driven packet-level simulator.
"""
from __future__ import annotations
from dataclasses import dataclass
import numpy as np

from trace.env.world import World, default_world
from trace.env.node import make_nodes
from trace.env import channel, arq
from trace.sim.metrics import Metrics

DEFAULT_PARAMS = dict(
    dz_max=100.0, N_tx_max=5.0, E_max=1000.0, Q_max=50, eta_th=0.40,
    weights=(0.35, 0.25, 0.15, 0.15, 0.10),
)


@dataclass
class SimResult:
    pdr: float
    mean_delay_s: float
    energy_per_bit_nj: float
    fnd_h: float
    lnd_h: float
    metrics: Metrics


def simulate(protocol, world: World = None, duration_h: float = 1.0,
             seed: int = 0, params: dict = None) -> SimResult:
    world = world or default_world(seed=seed)
    params = {**DEFAULT_PARAMS, **(params or {})}
    rng = np.random.default_rng(seed)
    nodes = make_nodes(world.node_positions)
    m = Metrics()
    K = len(nodes)
    n_packets = max(20, K * 2)
    max_hops = 6
    pkt_size_bits = 64 * 8
    P_tx_w = 2.0
    T_pkt = 64 * 8 / 10_000.0
    E_c = 1e-6

    for _ in range(n_packets):
        i = int(rng.integers(0, K))
        cur = nodes[i]
        hop = 0
        delay = 0.0
        total_energy = 0.0
        m.sent += 1
        while hop < max_hops:
            others = [n for n in nodes if n is not cur]
            best = protocol.choose_forwarder(cur, others, params)
            if best is None:
                break
            j = nodes[best["id"]]
            d = np.linalg.norm(cur.xyz - j.xyz)
            delay += d / 1500.0 + T_pkt
            per = channel.link_per(cur.xyz, j.xyz)
            ok, n_tx = arq.transmit(per, rng)
            spent = n_tx * (P_tx_w * T_pkt + E_c)
            total_energy += spent
            cur.E = max(cur.E - spent, 0.0)
            if not ok:
                break
            cur = j
            hop += 1
            if cur.xyz[2] < 60.0:
                m.delivered += 1
                m.delays_s.append(delay)
                m.per_delivery_energy_j.append(total_energy / pkt_size_bits)
                break

    return SimResult(pdr=m.pdr, mean_delay_s=m.mean_delay_s,
                     energy_per_bit_nj=m.energy_per_bit_nj,
                     fnd_h=m.fnd_h, lnd_h=m.lnd_h, metrics=m)
