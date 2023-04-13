from abc import ABC


class Thing(ABC):
    def __init__(self, name: str):
        self.name = name

