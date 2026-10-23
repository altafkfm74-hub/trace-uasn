"""
FISHER baseline.

    "Is FISHER All You Need in the Multi-AUV Underwater Target Tracking Task?"
"""
from trace.baselines.qe_orp import QEORPProtocol as _Base


class FISHERProtocol(_Base):
    name = "FISHER"
