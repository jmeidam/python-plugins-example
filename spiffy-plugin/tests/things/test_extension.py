from spiffy.things.extension import Extension


def test_nothing():
    x = Extension()
    x.set_x(5.0)

    assert x.x == 5.0
