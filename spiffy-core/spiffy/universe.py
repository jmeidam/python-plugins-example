from abc import ABC


class Entity(ABC):
    def __init__(self, name: str):
        self.name = name


class Universe:
    def __init__(self):
        self.space = {}

    def fill_space(self, entity: Entity):
        self.space[entity.name] = entity
