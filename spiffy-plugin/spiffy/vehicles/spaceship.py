from spiffy.universe import Entity


class SpaceShip(Entity):
    def __init__(self, name: str, length: float, v_max: float):
        super().__init__(name=name)
        self.length = length
        self.v_max = v_max
