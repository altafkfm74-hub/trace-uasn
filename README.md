# TRACE — Tracking-Regulated Multi-AUV Coordinated Localization-Confidence
#         and Energy-Efficient Cross-Layer Routing for Underwater Sensor Networks

Reference implementation of the method and of the ten baselines described in:

> A. Hussain, S. Li, M. Jamjoom, Z. Ullah,
> "TRACE: Tracking-Regulated Multi-AUV Coordinated Localization-Confidence
> and Energy-Efficient Cross-Layer Routing for Underwater Sensor Networks,"
> IEEE Transactions on ..., 2026.

## Repository layout

| Part | Module            | Purpose                                                                           |
|------|-------------------|-----------------------------------------------------------------------------------|
| I    | `trace.core`      | Every equation of Section III (IMM-PF, ToA+EKF, confidence, link, forwarder, coordination) |
| II   | `trace.env`       | World geometry, AUV trajectories, seabed sensors, acoustic channel, ARQ          |
| III  | `trace.sim`       | Packet-level event-driven simulator + metrics                                     |
| IV   | `trace.baselines` | Ten reference baseline protocols                                                  |
| V    | `scripts/`        | One Python script per Section IV figure                                           |

## Install

```bash
pip install -r requirements.txt
```

## 30-second demo

```python
from trace.env.world import default_world
from trace.sim.engine import simulate
from trace.baselines.trace_protocol import TRACEProtocol

world = default_world(seed=0, n_nodes=30)
r = simulate(protocol=TRACEProtocol(), world=world, duration_h=0.5, seed=0)
print(f"PDR={r.pdr:.3f}  delay={r.mean_delay_s:.2f}s  "
      f"E/bit={r.energy_per_bit_nj:.0f} nJ")
```

## Reproduce any figure

```bash
python scripts/fig01_reliability.py
```

Figures are written to `figures/`.

## Tests

```bash
pytest tests/ -q
```

## License

MIT — see `LICENSE`.
