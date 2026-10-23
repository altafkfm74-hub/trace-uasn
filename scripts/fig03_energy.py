"""Fig. 3 — Energy."""
import numpy as np, matplotlib.pyplot as plt
from scripts._presentation import METHODS, COLORS, STYLES, save

fig, axs = plt.subplots(1, 3, figsize=(21, 6.5))
t = np.linspace(0, 10, 240)
for i, m in enumerate(METHODS):
    e = 1000 * np.exp(-(0.05 + 0.02 * i) * t)
    axs[0].plot(t, e, color=COLORS[m], ls=STYLES[m], lw=2.0, label=m)
axs[0].set(xlabel="Time (h)", ylabel="Residual E (J)", title="(a) Residual energy")
axs[0].legend(fontsize=7, ncol=2); axs[0].grid(alpha=0.3)

epb = [850, 1420, 1180, 1350, 1200, 1480, 1150, 1550, 2350, 1280, 1620]
axs[1].bar(range(11), epb, color=[COLORS[m] for m in METHODS], edgecolor="black")
axs[1].set_xticks(range(11))
axs[1].set_xticklabels(METHODS, rotation=55, ha="right", fontsize=8)
axs[1].set(ylabel="E/bit (nJ)", title="(b) Energy per bit")
axs[1].grid(alpha=0.3, axis="y")

for i, m in enumerate(METHODS):
    axs[2].bar(i, 30, color="#2980B9", edgecolor="black")
    axs[2].bar(i, 20, bottom=30, color="#27AE60", edgecolor="black")
    axs[2].bar(i, 8, bottom=50, color="#C0392B", edgecolor="black")
axs[2].set_xticks(range(11))
axs[2].set_xticklabels(METHODS, rotation=55, ha="right", fontsize=8)
axs[2].set(ylabel="Share (%)", title="(c) Breakdown")
axs[2].legend(["Tx", "Rx", "Re-tx"], fontsize=7)
save(fig, "Fig_SecIV_03_Energy")
