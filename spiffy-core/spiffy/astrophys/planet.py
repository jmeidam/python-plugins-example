from spiffy.universe import Entity


class Planet(Entity):
    def __init__(self, name: str, radius: float, mass: float):
        super().__init__(name=name)
        self.radius = radius
        self.mass = mass
        self.surface_gravity = self._calc_a()

    def _calc_a(self) -> float:
        r2 = self.radius * self.radius
        a = self.mass / r2
        return a
