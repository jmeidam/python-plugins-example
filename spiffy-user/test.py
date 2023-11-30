from spiffy.universe import Universe
from spiffy.astrophys.star import Star
from spiffy.astrophys.blackhole import BlackHole
from spiffy.vehicles.spaceship import SpaceShip

universe1 = Universe()
star1 = Star("Star1", 1.1)
bh1 = BlackHole("BH1", 200.0, 0.8)
space_ship = SpaceShip("Spiffy", 500.0, 10.0)

universe1.fill_space(star1)
universe1.fill_space(bh1)
universe1.fill_space(space_ship)
print(f"Radius of Star1 is approximately {star1.radius}")
print(f"The spaceship Spiffy can travel at {space_ship.v_max} times the speed of light!")

for name, entity in universe1.space.items():
    print(f"Universe 1 contains {name}, which is of type {type(entity)}")
