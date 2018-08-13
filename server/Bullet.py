import math

from server.GameObject import GameObject
from Vector import Vector


class Bullet(GameObject):
    def __init__(self, position, radius, description="Bullet"):
        super(Bullet, self).__init__(position, description)
        self.radius = radius

    def vertices(self):
        for ang in range(8):
            my_ang = ang * math.pi / 8
            yield self.position + Vector(math.cos(my_ang), math.sin(my_ang)) * self.radius