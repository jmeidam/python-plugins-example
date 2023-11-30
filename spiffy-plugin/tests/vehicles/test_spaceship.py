from spiffy.vehicles.spaceship import SpaceShip


def test_something():
    x = SpaceShip("name", 22.0, 3.0)

    assert x.length == 22.0
    assert x.v_max == 3.0
