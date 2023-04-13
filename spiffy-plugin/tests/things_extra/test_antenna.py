from spiffy.things_extra.antenna import Antenna


def test_nothing():
    x = Antenna()
    x.set_height(5.0)

    assert x.height == 5.0
