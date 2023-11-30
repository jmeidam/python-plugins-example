from spiffy.universe import Entity


class BlackHole(Entity):
    def __init__(self, name: str, mass: float, spin: float):
        super().__init__(name=name)
        self.mass = mass
        self.spin = spin
        self.radius = self._calc_radius()

    def _calc_radius(self) -> float:
        return 2.0*self.mass
