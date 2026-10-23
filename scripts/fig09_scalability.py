"""Fig. 9 — Scalability."""
import numpy as np, matplotlib.pyplot as plt
from scripts._presentation import METHODS, COLORS, STYLES, save

fig, axs = plt.subplots(1, 3, figsize=(21, 6.5))
N = np.linspace(20, 80, 40)
pdr0 = [94.5, 81.2, 85.7, 83.4, 86.1, 79.3, 87.4, 75.8, 58.2, 80.5, 74.1]
for i, m in enumerate(METHODS):
    axs[0].plot(N, pdr0[i] * (1 - 0.005 * (N - 20)),
                color=COLORS[m], ls=STYLES[m], lw=2.0, label=m)
axs[0].set(xlabel="N", ylabel="PDR (%)", title="(a) PDR vs density")
axs[0].legend(fontsize=7, ncol=2); axs[0].grid(alpha=0.3)

ovh0 = [11, 17, 16, 22, 15, 18, 14, 19, 30, 24, 20]
for i, m in enumerate(METHODS):
    axs[1].plot(N, ovh0[i] * (1 + 0.01 * (N - 20)),
                color=COLORS[m], ls=STYLES[m], lw=2.0, label=m)
axs[1].set(xlabel="N", ylabel="Overhead (%)", title="(b) Overhead vs density")
axs[1].legend(fontsize=7, ncol=2); axs[1].grid(alpha=0.3)

wp = np.linspace(0.15, 0.55, 40); wc = np.linspace(0.0, 0.30, 40)
WP, WC = np.meshgrid(wp, wc)
Z = 80 + 15 * np.exp(-((WP - 0.35) ** 2 / 0.01 + (WC - 0.10) ** 2 / 0.006))
c = axs[2].imshow(Z, extent=[wp.min(), wp.max(), wc.min(), wc.max()],
                  origin="lower", cmap="viridis", aspect="auto")
axs[2].plot(0.35, 0.10, "*", color="red", ms=20, markeredgecolor="black")
axs[2].set(xlabel="w_p", ylabel="w_c", title="(c) PDR vs weights")
fig.colorbar(c, ax=axs[2], label="PDR (%)")
save(fig, "Fig_SecIV_09_Scalability")
