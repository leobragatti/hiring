import math

from .computed_property import computed_property


class Vector:
    def __init__(self, x, y, z, color=None):
        self.x, self.y, self.z = x, y, z
        self.color = color

    @computed_property("x", "y", "z")
    def magnitude(self):
        """
        Area magnitude
        """
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
