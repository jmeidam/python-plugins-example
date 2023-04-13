from spiffy.things.arm import Arm

def test_something():
    x = Arm()
    x.rotate(2)
    assert x.rotation == 2
    x.rotate(3)
    assert x.rotation == 5

