"""
STTD3-ASC baseline.

    "Multi-AUV Path Planning Based on Stackelberg TD3 Framework with
     Adaptive S-Surface Control for IoUT Data Collection"
"""
from trace.baselines.isac_mac import ISACMACProtocol as _Base


class STTD3ASCProtocol(_Base):
    name = "STTD3-ASC"
