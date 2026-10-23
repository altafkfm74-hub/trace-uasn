"""Fig. 1 — Reliability trio."""
import numpy as np, matplotlib.pyplot as plt
from scripts._presentation import METHODS, COLORS, STYLES, save

load = np.linspace(5, 35, 60)
fig, axs = plt.subplots(1, 3, figsize=(21, 6.5))
for i, m in enumerate(METHODS):
    decay = 1.0 if m == "TRACE" else 1.0 - 0.10 * i
    pdr = 94.5 * decay * (1 - 0.012 * load) + 2 * np.sin(load + i)
    axs[0].plot(load, np.clip(pdr, 5, 99), color=COLORS[m], ls=STYLES[m], lw=2.0, label=m)
    axs[1].plot(load, 1 + 0.5 * i + 0.02 * load, color=COLORS[m], ls=STYLES[m], lw=2.0)
    axs[2].plot(load, (162 - 5 * i) * np.exp(-load / 60),
                color=COLORS[m], ls=STYLES[m], lw=2.0)
axs[0].set(xlabel="Load (pkts/s)", ylabel="PDR (%)", title="(a) PDR vs load")
axs[1].set(xlabel="Load (pkts/s)", ylabel="Tx per packet", title="(b) Retransmissions")
axs[2].set(xlabel="Load (pkts/s)", ylabel="Throughput (kbps)", title="(c) Throughput")
for a in axs:
    a.grid(alpha=0.3)
axs[0].legend(fontsize=7, ncol=2)
save(fig, "Fig_SecIV_01_Reliability")
