from trace.core import forwarder


def test_score_bounds():
    s = forwarder.score(0.5, 0.2, 0.7, 0.1, 0.9)
    assert -1.0 < s < 1.0


def test_select():
    best = forwarder.select_forwarder(
        candidates=[
            {"id": "A", "z": 100, "E": 500, "q": 5, "E_Ntx": 1.2, "eta": 0.9},
            {"id": "B", "z": 120, "E": 800, "q": 2, "E_Ntx": 1.9, "eta": 0.5},
        ],
        z_i=200, dz_max=100, N_tx_max=5, E_max=1000, Q_max=50,
    )
    assert best["id"] == "A"
