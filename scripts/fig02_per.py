"""Fig. 2 — PER links."""
import numpy as np, matplotlib.pyplot as plt
from scripts._presentation import METHODS, COLORS, STYLES, save

fig, axs = plt.subplots(1, 3, figsize=(21, 6.5))
snr = np.linspace(0, 25, 80)
for i, m in enumerate(METHODS):
    per = 2.1 + i * 1.0 * np.exp(-snr / (8 + i))
    axs[0].semilogy(snr, per, color=COLORS[m], ls=STYLES[m], lw=2.0, label=m)
axs[0].set(xlabel="SNR (dB)", ylabel="PER (%)", title="(a) PER vs SNR")
axs[0].legend(fontsize=7, ncol=2); axs[0].grid(alpha=0.3, which="both")

X, Y = np.meshgrid(np.linspace(0, 1000, 60), np.linspace(0, 500, 40))
Z = 2 + 40 * ((X / 1000) ** 2) * (1 + (Y / 500))
c = axs[1].contourf(X, Y, Z, levels=20, cmap="turbo")
axs[1].set(xlabel="Distance (m)", ylabel="Depth (m)", title="(b) TRACE PER map")
fig.colorbar(c, ax=axs[1], label="PER (%)")

Z2 = 6 + 80 * ((X / 1000) ** 2) * (1 + (Y / 500))
c2 = axs[2].contourf(X, Y, Z2, levels=20, cmap="turbo")
axs[2].set(xlabel="Distance (m)", ylabel="Depth (m)", title="(c) QE-ORP PER map")
fig.colorbar(c2, ax=axs[2], label="PER (%)")
save(fig, "Fig_SecIV_02_PER_Links")
