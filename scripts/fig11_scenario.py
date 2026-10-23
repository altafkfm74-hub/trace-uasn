"""Fig. 11 — Scenario."""
import numpy as np, matplotlib.pyplot as plt
from scripts._presentation import METHODS, COLORS, save

fig, axs = plt.subplots(1, 3, figsize=(21, 6.5))
for a in axs:
    a.set_facecolor("#050A14"); a.set_xticks([]); a.set_yticks([])
    a.set_xlim(0, 1000); a.set_ylim(0, 500)

rng = np.random.default_rng(77)
for _ in range(14):
    axs[0].scatter(rng.uniform(60, 940), rng.uniform(60, 100),
                   s=40, color="#2ECC71", edgecolor="black")
for k in range(8):
    axs[0].scatter(rng.uniform(120, 880), rng.uniform(160, 400),
                   s=200, color=COLORS[METHODS[k]], edgecolor="black", marker=">")
axs[0].set_title("(a) Deployment", color="black")

for _ in range(10):
    axs[1].scatter(rng.uniform(60, 940), rng.uniform(60, 100),
                   s=30, color="#2ECC71", edgecolor="black")
axs[1].plot(np.linspace(200, 800, 80),
            250 + 80 * np.sin(np.linspace(0, 5, 80)),
            color="#FF0000", lw=2.0, label="true")
axs[1].plot(np.linspace(200, 800, 80),
            250 + 80 * np.sin(np.linspace(0, 5, 80)) + 10,
            color="#00FFFF", ls="--", lw=1.5, label="IMM-PF")
axs[1].legend(fontsize=8, labelcolor="white", facecolor="#1A1A1A")
axs[1].set_title("(b) Tracking", color="black")

axs[2].arrow(400, 300, 200, 100, head_width=15, color="#E74C3C")
axs[2].arrow(400, 300, 250, -80, head_width=15, color="#27AE60")
axs[2].set_title("(c) Cross-layer decision", color="black")
save(fig, "Fig_SecIV_11_Scenario")
