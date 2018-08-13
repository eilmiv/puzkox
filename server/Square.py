import math

from Vector import Vector
from server.GameObject import GameObject


class Square(GameObject):
    def __init__(self, position, site_length, description="Square"):
        super(Square, self).__init__(position, description)
        self.site_length = site_length

    @property
    def size(self):
        return Vector(self.site_length, self.site_length)

    def vertices(self):
        offsets = [Vector(1, 1), Vector(1, -1), Vector(-1, -1), Vector(-1, 1)]
        return [self.position + offset * self.site_length for offset in offsets]