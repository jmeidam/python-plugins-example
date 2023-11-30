from spiffy.astrophys.planet import Planet


def test_something():
    x = Planet(name="Omicron Persei VIII", radius=1.2, mass=0.8)
    assert x.name == "Omicron Persei VIII"
    assert x.radius == 1.2
    assert x.mass == 0.8
    assert x.surface_gravity == 0.8/(1.2*1.2)
