from spiffy.astrophys.blackhole import BlackHole


def test_something():
    x = BlackHole("BH1", 200.0, 0.75)

    assert x.spin == 0.75
    assert x.mass == 200.0
    assert x.radius == 400.0
