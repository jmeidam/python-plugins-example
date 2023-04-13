from spiffy.platform import Platform
from spiffy.things.arm import Arm

def test_something():
    x = Platform()
    y = Arm()
    x.fill_socket(y)

    assert isinstance(x.sockets[0], Arm)
