"""Fig. 6 — IMM-PF dynamics."""
import numpy as np, matplotlib.pyplot as plt
from scripts._presentation import METHODS, COLORS, STYLES, save

fig, axs = plt.subplots(1, 3, figsize=(21, 6.5))
t = np.linspace(0, 20, 400)
cv = 0.5 + 0.4 * np.sin(t / 3)
axs[0].stackplot(t, cv * 100, (1 - cv) * 100,
                 labels=["CV", "CT"], colors=["#2E86C1", "#E67E22"])
axs[0].set(xlabel="Time (s)", ylabel="Model prob (%)", title="(a) IMM")
axs[0].legend(fontsize=8); axs[0].grid(alpha=0.3)

r = 1.5 + 0.6 * np.sin(t)
axs[1].plot(t, r, color="#C0392B", lw=1.5, label="NIS")
ax2 = axs[1].twinx()
ax2.plot(t, np.exp(-r / 2) * 100, color="#1F618D", ls="--", label="q_k")
axs[1].set(xlabel="Time (s)", ylabel="NIS", title="(b) Residual / quality")
axs[1].legend(fontsize=8, loc="upper left"); axs[1].grid(alpha=0.3)

e = np.linspace(0, 12, 200)
head0 = [1.1, 2.4, 2.0, 3.1, 2.4, 1.9, 2.6, 3.0, 5.2, 3.4, 2.6]
for i, m in enumerate(METHODS):
    axs[2].plot(e, 100 * (1 - np.exp(-e / head0[i])),
                color=COLORS[m], ls=STYLES[m], lw=2.0, label=m)
axs[2].set(xlabel="Heading error (deg)", ylabel="CDF (%)",
           title="(c) Heading CDF")
axs[2].legend(fontsize=7, ncol=2); axs[2].grid(alpha=0.3)
save(fig, "Fig_SecIV_06_IMMPF_Dynamics")
