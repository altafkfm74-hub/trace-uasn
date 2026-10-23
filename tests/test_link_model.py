from trace.core import link_model


def test_per_energy():
    p = link_model.per_from_ack(90, 100)
    assert abs(p - 0.10) < 1e-9
    EN = link_model.expected_transmissions(0.10)
    assert abs(EN - 1 / 0.9) < 1e-9
    e = link_model.energy_per_packet(EN, 2.0, 0.1, 1e-6)
    assert e > 0
