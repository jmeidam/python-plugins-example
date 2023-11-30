from spiffy.universe import Entity


class Shuttle(Entity):
    def __init__(self, name: str, capacity: int):
        super().__init__(name=name)
        self.capacity = capacity
