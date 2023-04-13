from spiffy.things.thing import Thing


class Arm(Thing):
    def __init__(self):
        super().__init__(name='arm')
        self.rotation = 0

    def rotate(self, n: int):
        self.rotation += n
