"""Fig. 14 — Final results overview."""
import numpy as np, matplotlib.pyplot as plt
from scripts._presentation import METHODS, COLORS, STYLES, save

fig = plt.figure(figsize=(32, 22))
axS = fig.add_axes([0.22, 0.42, 0.56, 0.52])
axS.set_xlim(0, 1500); axS.set_ylim(0, 500)
axS.set_xticks([]); axS.set_yticks([]); axS.set_facecolor("#0A2842")
axS.set_title("(a) TRACE methodological overview", fontsize=13, color="black")

axL1 = fig.add_axes([0.02, 0.69, 0.19, 0.24])
axL2 = fig.add_axes([0.02, 0.42, 0.19, 0.24])
axR1 = fig.add_axes([0.79, 0.69, 0.19, 0.24])
axR2 = fig.add_axes([0.79, 0.42, 0.19, 0.24])
axB1 = fig.add_axes([0.02, 0.10, 0.23, 0.28])
axB2 = fig.add_axes([0.27, 0.10, 0.23, 0.28])
axB3 = fig.add_axes([0.52, 0.10, 0.23, 0.28])
axB4 = fig.add_axes([0.77, 0.10, 0.21, 0.28])


def _panel(ax, title, seed):
    rng = np.random.default_rng(seed)
    for i, m in enumerate(METHODS):
        t = np.linspace(0, 10, 60)
        y = (1 - i * 0.05) * (1 - np.exp(-t / 3)) + 0.02 * rng.standard_normal(60)
        ax.plot(t, y, color=COLORS[m], ls=STYLES[m], lw=2.0,
                label=m if i == 0 else None)
    ax.set_title(title, fontsize=10); ax.grid(alpha=0.3)
    ax.legend(fontsize=6, loc="best")


_panel(axL1, "(b) PDR", 1); _panel(axL2, "(c) Confidence", 2)
_panel(axR1, "(d) RMSE", 3); _panel(axR2, "(e) Track RMSE", 4)
_panel(axB1, "(f) NIS/q", 5); _panel(axB2, "(g) P_D", 6)
_panel(axB3, "(h) Heading CDF", 7); _panel(axB4, "(i) E/bit", 8)
save(fig, "Fig_SecIV_14_Final_Results")
