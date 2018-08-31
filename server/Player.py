from Vector import Vector
from server.GameObject import GameObject
from math import cos, sin, pi
import server.options as options
from server.House import House
from time import time
from server.Bullet import Bullet
import server.options as options


class Player (GameObject):
    def __init__(self, position, angle, size=options.player_size, description="Player"):
        super(Player, self).__init__(position, description)

        self.health = options.player_health
        self.energy = 0
        self.charges = 0

        self.proportion = size.x / (2 * size.y)  # length to half width ratio
        self.position2 = position - Vector(cos(angle + pi / 2), sin(angle + pi / 2)) * size.y
        self.size = size

        self.forward = False
        self.backward = False
        self.right = False
        self.left = False

        self.client = None
        self.world = None

    def vertices(self):
        half_width = (self.position2 - self.position).rotate90() * self.proportion
        yield self.position + half_width
        yield self.position - half_width
        yield self.position2 - half_width
        yield self.position2 + half_width

    def update(self, colliding):
        for o in colliding:
            if isinstance(o, House):
                o.last_hit = time()
            elif isinstance(o, Bullet):
                if o.exist:
                    self.health -= options.bullet_damage
                    print(self.health)
                    if self.health <= 0:
                        self.die()
                    o.exist = False

    def die(self):
        self.updating = False
        print("Toooooot!!!!!!!!!!!!!!!!!!!!!")

    def move(self, delta_t):
        if self.forward:
            self.position += Vector(0, 1) * delta_t * options.player_speed
        if self.backward:
            self.position += Vector(0, -1) * delta_t * options.player_speed
        if self.right:
            self.position += Vector(1, 0) * delta_t * options.player_speed
        if self.left:
            self.position += Vector(-1, 0) * delta_t * options.player_speed

        a = abs(self.position2-self.position)
        if a == 0:
            self.position2 = self.position-Vector(0, -self.size.y)
        else:
            self.position2 = self.position + (self.position2-self.position) * (self.size.y / a)

    def serialize(self):
        location = (self.position+self.position2)/2
        r_ang = self.position-self.position2
        ang = Vector(1, 0).ang(r_ang)
        ang = ang/(2*pi)*360
        if Vector(0, 1) * r_ang < 0:
            ang = 360-ang
        return {"location_x":location.x, "location_y":location.y, "angle":ang-90, "texture":"car", "damage":1, "foreground":True}

    def shoot(self):
        velocity = self.position-self.position2
        velocity_normiert = (velocity)*(1/abs(velocity))
        bullet = Bullet(self.position+velocity_normiert * (options.bullet_radius+0.01), options.bullet_radius,
                        velocity_normiert*options.bullet_speed)
        self.world.add(bullet)

        # fliegt unendlich weit



if __name__ == "__main__":
    pass