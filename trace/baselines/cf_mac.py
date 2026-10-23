"""
CF-MAC baseline.

    "A Mobility-Aware Conflict-Graph Scheduling Framework for AUV-Assisted
     Collaborative Underwater Acoustic Networks"
"""
from trace.baselines.qe_orp import QEORPProtocol as _Base


class CFMACProtocol(_Base):
    name = "CF-MAC"
