"""Fig. 5 — Localization accuracy."""
import numpy as np, matplotlib.pyplot as plt
from scripts._presentation import METHODS, COLORS, STYLES, save

fig, axs = plt.subplots(1, 3, figsize=(21, 6.5))
n = np.linspace(1, 8, 40)
rmse0 = [1.8, 2.8, 3.5, 4.1, 3.2, 2.6, 3.0, 3.8, 6.4, 4.4, 3.2]
for i, m in enumerate(METHODS):
    axs[0].plot(n, rmse0[i] * (1 + 1.2 * np.exp(-n / 3)),
                color=COLORS[m], ls=STYLES[m], lw=2.0, label=m)
axs[0].set(xlabel="AUVs", ylabel="RMSE (m)", title="(a) RMSE vs fleet")
axs[0].legend(fontsize=7, ncol=2); axs[0].grid(alpha=0.3)

e = np.linspace(0, 25, 200)
for i, m in enumerate(METHODS):
    axs[1].plot(e, 100 * (1 - np.exp(-(e / (rmse0[i] * 2)) ** 2)),
                color=COLORS[m], ls=STYLES[m], lw=2.0, label=m)
axs[1].set(xlabel="Error (m)", ylabel="CDF (%)", title="(b) Error CDF")
axs[1].legend(fontsize=7, ncol=2); axs[1].grid(alpha=0.3)

X, Y = np.meshgrid(np.linspace(0, 1000, 60), np.linspace(0, 500, 40))
Z = 0.94 - 0.45 * np.exp(-((X - 500) ** 2 + (Y - 250) ** 2) / (2 * 380 ** 2))
c = axs[2].imshow(Z, extent=[0, 1000, 0, 500], origin="lower",
                  cmap="RdYlGn", aspect="auto")
axs[2].set(xlabel="X (m)", ylabel="Y (m)", title=r"(c) Confidence $\eta$")
fig.colorbar(c, ax=axs[2], label=r"$\eta$")
save(fig, "Fig_SecIV_05_Localization")
