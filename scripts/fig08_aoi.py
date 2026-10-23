"""Fig. 8 — AoI."""
import numpy as np, matplotlib.pyplot as plt
from scripts._presentation import METHODS, COLORS, STYLES, save

fig, axs = plt.subplots(1, 3, figsize=(21, 6.5))
t = np.linspace(0, 3600, 500)
aoi0 = [840, 1920, 1320, 2280, 1200, 1800, 1080, 1680, 3480, 2040, 1560]
for i, m in enumerate(METHODS):
    y = aoi0[i] * (0.5 + 0.5 * (1 - np.exp(-t / 2000)))
    axs[0].plot(t, y, color=COLORS[m], ls=STYLES[m], lw=2.0, label=m)
axs[0].set(xlabel="Time (s)", ylabel="AoI (s)", title="(a) AoI temporal")
axs[0].legend(fontsize=7, ncol=2); axs[0].grid(alpha=0.3)

src = np.linspace(1, 10, 30)
for i, m in enumerate(METHODS):
    axs[1].plot(src, aoi0[i] * (1 + 0.05 * np.log(src)),
                color=COLORS[m], ls=STYLES[m], lw=2.0, label=m)
axs[1].set(xlabel="Source rank", ylabel="AoI (s)", title="(b) AoI vs source")
axs[1].legend(fontsize=7, ncol=2); axs[1].grid(alpha=0.3)

X, Y = np.meshgrid(np.linspace(0, 1000, 60), np.linspace(0, 500, 40))
Z = 60 + 900 * (1 - np.exp(-((X - 500) ** 2 + (Y - 250) ** 2) / (2 * 380 ** 2)))
c = axs[2].imshow(Z, extent=[0, 1000, 0, 500], origin="lower",
                  cmap="magma", aspect="auto")
axs[2].set(xlabel="X (m)", ylabel="Y (m)", title="(c) AoI spatial")
fig.colorbar(c, ax=axs[2], label="AoI (s)")
save(fig, "Fig_SecIV_08_AoI")
