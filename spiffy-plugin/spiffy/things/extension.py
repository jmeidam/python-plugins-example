from spiffy.things.thing import Thing


class Extension(Thing):
    def __init__(self):
        super().__init__(name='extension')
        self.x = 0
        self.info = 'info'

    def set_x(self, n: float):
        self.x = n
