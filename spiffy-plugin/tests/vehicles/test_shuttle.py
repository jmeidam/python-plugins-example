from spiffy.vehicles.shuttle import Shuttle


def test_something():
    x = Shuttle("name", 5)

    assert x.capacity == 5
