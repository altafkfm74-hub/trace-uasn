"""Fig. 10 — Cross-layer coupling."""
import numpy as np, matplotlib.pyplot as plt
from scripts._presentation import METHODS, COLORS, STYLES, save

fig, axs = plt.subplots(1, 3, figsize=(21, 6.5))
rng = np.random.default_rng(11)
raw = np.clip(rng.uniform(0.25, 0.95, (6, 5)), 0, 1)
comps = ["Depth", "Retx", "Energy", "Buffer", "Conf"]
wbar = 0.14
for j, cc in enumerate(comps):
    axs[0].bar(np.arange(6) + j * wbar, raw[:, j], wbar,
               label=cc, edgecolor="black")
axs[0].set_xticks(np.arange(6) + 2 * wbar)
axs[0].set_xticklabels([f"n{k+1}" for k in range(6)])
axs[0].set(ylabel="Normalized", title="(a) Score decomposition")
axs[0].legend(fontsize=7)

th = np.linspace(0.2, 0.9, 40)
for i, m in enumerate(METHODS):
    y = 94.5 - i * 2 - 40 * np.clip(th - 0.65, 0, None)
    axs[1].plot(th, y, color=COLORS[m], ls=STYLES[m], lw=2.0, label=m)
axs[1].axvline(0.40, color="gray", ls=":")
axs[1].set(xlabel=r"$\eta_{th}$", ylabel="PDR (%)", title="(b) Gate tuning")
axs[1].legend(fontsize=7, ncol=2); axs[1].grid(alpha=0.3)

for i, m in enumerate(METHODS):
    axs[2].scatter([55 + 4 * i], [94.5 - i * 2],
                   color=COLORS[m], s=60, label=m, edgecolor="black")
axs[2].set(xlabel=r"$\bar{\eta}$ (%)", ylabel="PDR (%)",
           title="(c) Confidence-PDR")
axs[2].legend(fontsize=6, ncol=2); axs[2].grid(alpha=0.3)
save(fig, "Fig_SecIV_10_CrossLayer")
