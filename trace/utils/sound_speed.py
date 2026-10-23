"""Mackenzie sound-speed profile."""


def mackenzie(T: float, S: float, z: float) -> float:
    return float(1449.2 + 4.6 * T - 0.055 * T ** 2 + 0.00029 * T ** 3
                 + (1.34 - 0.01 * T) * (S - 35.0) + 0.016 * z)
