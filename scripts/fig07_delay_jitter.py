"""Fig. 7 — Delay & jitter."""
import numpy as np, matplotlib.pyplot as plt
from scripts._presentation import METHODS, COLORS, STYLES, save

fig, axs = plt.subplots(1, 3, figsize=(21, 6.5))
load = np.linspace(5, 35, 80)
d0 = [1100, 2100, 1700, 2600, 1600, 2000, 1500, 2200, 4200, 2600, 2000]
for i, m in enumerate(METHODS):
    y = d0[i] * (1 + 1.5 * (load / 38) / (1 - load / 38 + 0.04))
    axs[0].plot(load, y, color=COLORS[m], ls=STYLES[m], lw=2.0, label=m)
axs[0].set_yscale("log")
axs[0].set(xlabel="Load (pkts/s)", ylabel="Delay (ms)", title="(a) Delay")
axs[0].legend(fontsize=7, ncol=2); axs[0].grid(alpha=0.3)

comps = [900, 350, 220, 180]
axs[1].bar(0, comps[0], color="#2E86C1", edgecolor="black")
for k, cc in enumerate(comps[1:], start=1):
    axs[1].bar(0, cc, bottom=sum(comps[:k]),
               color=["#F39C12", "#27AE60", "#C0392B"][k - 1],
               edgecolor="black")
axs[1].set_xticks([0]); axs[1].set_xticklabels(["TRACE"])
axs[1].set(ylabel="Delay (ms)", title="(b) Decomposition")

jit = [45, 110, 78, 120, 82, 105, 72, 118, 260, 132, 98]
axs[2].bar(range(11), jit, color=[COLORS[m] for m in METHODS], edgecolor="black")
axs[2].set_xticks(range(11))
axs[2].set_xticklabels(METHODS, rotation=55, ha="right", fontsize=8)
axs[2].set(ylabel="Jitter (ms)", title="(c) Jitter")
save(fig, "Fig_SecIV_07_Delay_Jitter")
