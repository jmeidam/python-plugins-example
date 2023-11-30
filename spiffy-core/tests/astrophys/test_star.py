from spiffy.astrophys.star import Star


def test_something():
    x = Star("twinkle", 1.1)
    assert x.radius == 1.1**0.8
    assert x.name == "twinkle"
