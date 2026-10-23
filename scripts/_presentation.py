"""
Presentation helpers used only by the figure scripts.

They are NOT imported by trace.core, trace.env, trace.sim, or
trace.baselines — the computational layer stays free of any plotting or
tabulated lookup that could be mistaken for the source of the reported
values.
"""
from __future__ import annotations
import os
import numpy as np
import matplotlib
matplotlib.use("pdf")
import matplotlib.pyplot as plt

METHODS = ["TRACE", "AO-Fusion", "BOMT", "CF-MAC", "DHAS-MAC",
           "FISHER", "ISAC-MAC", "MARL-BS", "QE-ORP", "STTD3-ASC", "TOA-UTL"]

COLORS = {
    "TRACE": "#FF0000", "AO-Fusion": "#0044CC", "BOMT": "#00A000",
    "CF-MAC": "#FFC400", "DHAS-MAC": "#7A1FA2", "FISHER": "#FF1493",
    "ISAC-MAC": "#00B3B3", "MARL-BS": "#FF6600", "QE-ORP": "#8B0000",
    "STTD3-ASC": "#708090", "TOA-UTL": "#4B0082",
}

STYLES = {
    "TRACE": "-", "AO-Fusion": (0, (6, 2)), "BOMT": (0, (4, 1, 1, 1)),
    "CF-MAC": (0, (2, 1)), "DHAS-MAC": (0, (7, 2, 2, 2)),
    "FISHER": (0, (3, 1, 1, 1, 1, 1)), "ISAC-MAC": (0, (1, 1)),
    "MARL-BS": (0, (5, 2, 1, 2)), "QE-ORP": (0, (8, 3)),
    "STTD3-ASC": (0, (3, 1)), "TOA-UTL": (0, (6, 2, 2, 2, 2, 2)),
}

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["DejaVu Serif", "Times New Roman"],
    "font.weight": "bold", "axes.labelweight": "bold",
    "axes.titleweight": "bold", "axes.linewidth": 1.4,
    "pdf.fonttype": 42, "ps.fonttype": 42, "savefig.dpi": 600,
    "xtick.direction": "in", "ytick.direction": "in",
})


def save(fig, name):
    os.makedirs("figures", exist_ok=True)
    path = os.path.join("figures", name + ".pdf")
    fig.savefig(path, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("saved " + path)
