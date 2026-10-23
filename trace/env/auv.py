"""
AUV trajectory classes matching Table (tab:auv_coordination).
"""
from __future__ import annotations
from dataclasses import dataclass
import numpy as np


@dataclass
class AUVSpec:
    name: str
    x_center: float
    z_band: tuple
    trajectory: str


AUV_FLEET = [
    AUVSpec("AUV1", 250,  (200, 300), "raster"),
    AUVSpec("AUV2", 450,  (200, 300), "raster2"),
    AUVSpec("AUV3", 700,  (100, 200), "orbit"),
    AUVSpec("AUV4", 900,  (150, 350), "spiral"),
    AUVSpec("AUV5", 1050, (250, 400), "spiral_deep"),
    AUVSpec("AUV6", 1200, (200, 250), "perimeter"),
    AUVSpec("AUV7", 1330, (200, 250), "antipodal"),
    AUVSpec("AUV8", 500,  (50, 450),  "elevator"),
]


def position_at(spec: AUVSpec, t: float, W: float = 1500.0) -> tuple:
    """Return (x, y, z) of the AUV at time t (seconds)."""
    zc = 0.5 * (spec.z_band[0] + spec.z_band[1])
    phase = (t / 200.0) % 1.0
    if spec.trajectory in ("raster", "raster2"):
        x = spec.x_center + 60 * np.sin(2 * np.pi * phase)
        y = 500.0 + 80 * np.sin(2 * np.pi * 2 * phase)
    elif spec.trajectory == "orbit":
        a = 2 * np.pi * phase
        x = spec.x_center + 300 * np.cos(a)
        y = 500.0 + 150 * np.sin(a)
    elif spec.trajectory in ("spiral", "spiral_deep"):
        a = (4 * np.pi if spec.trajectory == "spiral" else -4 * np.pi) * phase
        r = 90 + 60 * np.sin(2 * np.pi * phase)
        x = spec.x_center + r * np.cos(a)
        y = 500.0 + r * 0.6 * np.sin(a)
    elif spec.trajectory == "perimeter":
        a = 2 * np.pi * phase
        x = spec.x_center + 90 * np.cos(a)
        y = 500.0 + 300 * np.sin(a)
    elif spec.trajectory == "antipodal":
        a = 2 * np.pi * phase + np.pi
        x = spec.x_center + 90 * np.cos(a)
        y = 500.0 + 300 * np.sin(a)
    else:  # elevator
        u = 0.5 * (1 - np.cos(2 * np.pi * phase))
        z_lo, z_hi = spec.z_band
        return (spec.x_center, 500.0, z_lo + u * (z_hi - z_lo))
    x = float(np.clip(x, 20, W - 20))
    y = float(np.clip(y, 20, 980))
    return x, y, float(zc)
