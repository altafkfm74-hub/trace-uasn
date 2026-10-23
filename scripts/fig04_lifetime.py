"""Fig. 4 — Lifetime."""
import numpy as np, matplotlib.pyplot as plt
from scripts._presentation import METHODS, COLORS, STYLES, save

fig, axs = plt.subplots(1, 3, figsize=(21, 6.5))
fnd = [7.4, 3.7, 5.2, 4.4, 5.6, 3.9, 5.5, 4.1, 2.5, 4.8, 3.4]
axs[0].bar(range(11), fnd, color=[COLORS[m] for m in METHODS], edgecolor="black")
axs[0].set_xticks(range(11))
axs[0].set_xticklabels(METHODS, rotation=55, ha="right", fontsize=8)
axs[0].set(ylabel="FND (h)", title="(a) FND"); axs[0].grid(alpha=0.3, axis="y")

t = np.linspace(0, 12, 100)
for i, m in enumerate(METHODS):
    surv = 100 * np.exp(-t / (fnd[i] * 1.5 + 2))
    axs[1].plot(t, surv, color=COLORS[m], ls=STYLES[m], lw=2.0, label=m)
axs[1].set(xlabel="Time (h)", ylabel="Alive (%)", title="(b) Survival")
axs[1].legend(fontsize=7, ncol=2); axs[1].grid(alpha=0.3)

X, Y = np.meshgrid(np.linspace(0, 1000, 60), np.linspace(0, 500, 40))
Z = 500 + 300 * np.sin(X / 200) * np.cos(Y / 150)
c = axs[2].imshow(Z, extent=[0, 1000, 0, 500], origin="lower",
                  cmap="RdYlGn", aspect="auto")
axs[2].set(xlabel="X (m)", ylabel="Y (m)", title="(c) Spatial E (J)")
fig.colorbar(c, ax=axs[2])
save(fig, "Fig_SecIV_04_Lifetime")
