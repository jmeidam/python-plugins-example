from spiffy.universe import Universe
from spiffy.astrophys.star import Star


def test_something():
    x = Universe()
    y = Star(name="twinkle", mass=1.1)
    x.fill_space(y)

    assert isinstance(x.space["twinkle"], Star)
