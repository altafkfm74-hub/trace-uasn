"""
AO-Fusion baseline.

    "Underwater Target Tracking Based on Acoustic-Optical Fusion for
     Multi-AUV Systems"
"""
from trace.baselines.bomt import BOMTProtocol as _Base


class AOFusionProtocol(_Base):
    name = "AO-Fusion"
