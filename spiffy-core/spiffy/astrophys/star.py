from spiffy.universe import Entity


class Star(Entity):
    def __init__(self, name: str, mass: float):
        """Mass and radius in Solar units"""
        super().__init__(name=name)
        self.mass = mass
        self.type = "Main Sequence"
        self.radius = self._calculate_radius()

    def _calculate_radius(self) -> float:
        radius = self.mass**0.8
        return radius
