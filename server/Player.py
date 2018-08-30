from Vector import Vector
from server.GameObject import GameObject
from math import cos, sin, pi


class Player (GameObject):
    def __init__(self, position, angle, size=Vector(0.5, 0.25), description="Player"):
        super(Player, self).__init__(position, description)

        self.health = 0
        self.energy = 0
        self.charges = 0

        self.proportion = size.x / (2 * size.y)  # length to half width ratio
        self.position2 = position - Vector(cos(angle + pi / 2), sin(angle + pi / 2)) * size.y
        self.size = size
        self.client = None

    def vertices(self):
        half_width = (self.position2 - self.position).rotate90() * self.proportion
        yield self.position + half_width
        yield self.position - half_width
        yield self.position2 - half_width
        yield self.position2 + half_width

    def update(self):
        pass

if __name__ == "__main__":
    print("hi")
