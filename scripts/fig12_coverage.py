"""Fig. 12 — Coverage."""
import numpy as np, matplotlib.pyplot as plt
from scripts._presentation import METHODS, COLORS, STYLES, save

fig, axs = plt.subplots(1, 3, figsize=(21, 6.5))
rev0 = [18, 28, 22, 27, 23, 28, 22, 26, 45, 30, 27]
axs[0].bar(range(11), rev0,
           color=[COLORS[m] for m in METHODS], edgecolor="black")
axs[0].set_xticks(range(11))
axs[0].set_xticklabels(METHODS, rotation=55, ha="right", fontsize=8)
axs[0].set(ylabel="Revisit (min)", title="(a) Revisit time")

t = np.linspace(0, 10, 240)
cov0 = [92, 74, 82, 76, 84, 78, 83, 72, 55, 73, 76]
for i, m in enumerate(METHODS):
    axs[1].plot(t, cov0[i] * (1 - np.exp(-t / 3)),
                color=COLORS[m], ls=STYLES[m], lw=2.0, label=m)
axs[1].set(xlabel="Time (h)", ylabel="Coverage (%)", title="(b) Coverage growth")
axs[1].legend(fontsize=7, ncol=2); axs[1].grid(alpha=0.3)

X, Y = np.meshgrid(np.linspace(0, 1000, 60), np.linspace(0, 500, 40))
Z = np.exp(-((X - 300) ** 2 + (Y - 250) ** 2) / (2 * 200 ** 2))     + np.exp(-((X - 700) ** 2 + (Y - 250) ** 2) / (2 * 200 ** 2))
c = axs[2].imshow(Z, extent=[0, 1000, 0, 500], origin="lower",
                  cmap="viridis", aspect="auto")
axs[2].set(xlabel="X (m)", ylabel="Y (m)", title="(c) Density")
fig.colorbar(c, ax=axs[2], label="Density")
save(fig, "Fig_SecIV_12_Coverage")
