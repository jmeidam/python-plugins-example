from spiffy.things.thing import Thing

def test_something():
    x = Thing('test')
    assert x.name == 'test'
