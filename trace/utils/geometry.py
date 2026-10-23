"""Small geometry helpers."""
import numpy as np


def dist(a, b) -> float:
    return float(np.linalg.norm(np.asarray(a, float) - np.asarray(b, float)))


def unit(a, b) -> np.ndarray:
    d = np.asarray(a, float) - np.asarray(b, float)
    r = max(np.linalg.norm(d), 1e-12)
    return d / r
