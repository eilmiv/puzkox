from Vector import Vector
from server.GameObject import GameObject


class Player (GameObject):
    def __init__(self, position, angle, size, offset, description="Player"):
        super(Player, self).__init__(self, position, description)
        self.health = 0
        self.energy = 0
        self.charges = 0
        self.angle = angle
        self.size = size
        self.offset = offset

    def vertices(self):
        r = self.size / 2
        offsets = [Vector(r.x, -r.y), r, Vector(-r.x, r.y), -r]
        return [self.position + self.offset + offset for offset in offsets]

    def update(self):
        pass

if __name__ == "__main__":
    print("hi")
