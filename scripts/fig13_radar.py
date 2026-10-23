"""Fig. 13 — Radar dashboard (8 AUVs)."""
import numpy as np, matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge
from scripts._presentation import METHODS, COLORS, save

names = ["AUV1", "AUV2", "AUV3", "AUV4",
         "AUV5", "AUV6", "AUV7", "AUV8"]
fig = plt.figure(figsize=(26, 10.5))
gs = fig.add_gridspec(2, 8, hspace=0.16, wspace=0.20)

for c in range(8):
    ax = fig.add_subplot(gs[0, c]); ax.set_facecolor("#02080E")
    ax.set_xlim(-1.15, 1.15); ax.set_ylim(-1.15, 1.15)
    ax.set_aspect("equal"); ax.set_xticks([]); ax.set_yticks([])
    for r in [0.25, 0.5, 0.75, 1.0]:
        ax.add_patch(Circle((0, 0), r, fill=False, ec="#1F7A5A",
                            lw=0.6, alpha=0.5))
    for k in range(24):
        ang = np.radians((c * 45 - k * 3) % 360)
        ax.add_patch(Wedge((0, 0), 1.0,
                           np.degrees(ang), np.degrees(ang) + 3,
                           fc="#00FFB3", ec="none", alpha=0.06 * (1 - k / 24)))
    ang = np.radians((c * 45 + 20) % 360)
    ax.plot([0, np.cos(ang)], [0, np.sin(ang)],
            color="#7FFFD4", lw=1.2, alpha=0.9)
    rng = np.random.default_rng(c + 100)
    for _ in range(6):
        r = rng.uniform(0.3, 0.95); a = rng.uniform(0, 2 * np.pi)
        ax.plot(r * np.cos(a), r * np.sin(a),
                "x", color="#FF4B3E", ms=5, mew=1.1)
    ax.plot(0, 0, "o", ms=6, mfc="#FFD700", mec="black", mew=0.9)
    ax.text(0, -1.1, names[c], fontsize=8, fontweight="bold",
            color=COLORS[METHODS[c]], ha="center",
            bbox=dict(fc="#02080E", ec=COLORS[METHODS[c]], lw=0.5))

    ax2 = fig.add_subplot(gs[1, c]); ax2.set_facecolor("#04101E")
    ax2.set_xlim(0, 1000); ax2.set_ylim(0, 500)
    ax2.set_xticks([]); ax2.set_yticks([])
    t = np.linspace(0, 1, 100)
    x = 200 + 600 * t + 30 * np.sin(6 * np.pi * t + c)
    y = 100 + 300 * t + 50 * np.cos(2 * np.pi * t + c)
    ax2.plot(x, y, color=COLORS[METHODS[c]], lw=1.5, alpha=0.9)
    ax2.set_title(names[c] + " top-view", fontsize=8,
                  color=COLORS[METHODS[c]], fontweight="bold")

save(fig, "Fig_SecIV_13_Radar_8AUV")
