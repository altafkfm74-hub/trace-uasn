from trace.core import collision


def test_collision_safe():
    assert collision.collision_condition(200, 300, [0, 0, 200], [0, 0, 300]) is True


def test_slot_ok():
    assert collision.interference_free(0.0, 2.0, 1500, 1500) is True


def test_measurement_set():
    assert collision.measurement_set([0, 0, 100],
                                     [[0, 0, 50], [500, 0, 50]]) == [0]
