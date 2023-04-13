from spiffy.things.thing import Thing


class Antenna(Thing):
    def __init__(self):
        super().__init__(name='antenna')
        self.height = 0

    def set_height(self, h: float):
        self.height = h
