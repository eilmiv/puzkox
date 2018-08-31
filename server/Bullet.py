import math

from server.GameObject import GameObject
from Vector import Vector
from server.options import bullet_damage


class Bullet(GameObject):
    def __init__(self, position, radius, velocity, description="Bullet"):
        super(Bullet, self).__init__(position, description)
        self.radius = radius
        self.velocity = velocity
        self.world_size = Vector(10, 10)

    def vertices(self):
        for ang in range(8):
            my_ang = ang * math.pi / 4
            yield self.position + Vector(math.cos(my_ang), math.sin(my_ang)) * self.radius

    def move(self, delta_t):
        old_position = self.position
        self.position=self.position + self.velocity * delta_t
        if not (0 <= round(self.position.x) < (self.world_size.x)) or not (0 <= round(self.position.y) < (self.world_size.y)):
            self.exist = False
            self.position = old_position


    def update(self, colliding):
        pass

    def serialize(self):
        return {"location_x":self.position.x, "location_y":self.position.y, "texture":"bullet", "foreground":True,
                "radius":self.radius}
