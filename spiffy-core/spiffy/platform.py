from spiffy.things.thing import Thing


class Platform:
    def __init__(self):
        self.sockets = []

    def fill_socket(self, thing: Thing):
        self.sockets.append(thing)
