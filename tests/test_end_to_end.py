from trace.env.world import default_world
from trace.sim.engine import simulate
from trace.baselines.trace_protocol import TRACEProtocol


def test_tiny_simulation_runs():
    world = default_world(seed=0, n_nodes=8)
    r = simulate(protocol=TRACEProtocol(), world=world,
                 duration_h=0.1, seed=0)
    assert 0.0 <= r.pdr <= 1.0
    assert r.mean_delay_s >= 0.0
    assert r.energy_per_bit_nj >= 0.0
