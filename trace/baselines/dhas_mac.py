"""
DHAS-MAC baseline.

    "DQN-Based Underwater Acoustic MAC Protocol with a Dynamic
     Hierarchical Authorization System"
"""
from trace.baselines.qe_orp import QEORPProtocol as _Base


class DHASMACProtocol(_Base):
    name = "DHAS-MAC"
