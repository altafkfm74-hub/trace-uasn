"""
TOA-UTL baseline (localization reference).

    "A Shifted-Gamma Noise Model for Practical Underwater Acoustic
     Target Localization"
"""
from trace.sim.protocol import TRACEProtocol as _T


class TOAUTLProtocol(_T):
    name = "TOA-UTL"
