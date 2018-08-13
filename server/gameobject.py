import Vector
class gameobject:
    def __init__(self, position, is_circle, angle, size, offset, description):
        self._position = position
        self.is_circle = is_circle
        self.size = size
        self.offset = offset
        self.angle = angle
        self.description = description

    @property
    def position(self):
        return self._position

    @position.setter
    def set_position (self, new_position):
        self._position = new_position

    def colliding(self, other):
        if self.is_circle and other.is_cicrcle:
            return abs(self.position - other.position) >= (self.size.x + other.size.x) / 2
        elif not self.is_circle and not other.is_cicrcle:
            return (self.position.x < other.position.x + other.size.x and self.position.x + self.size.x > other.position.x) \
            and \
            (self.position.y < other.position.y + other.size.y and self.position.y + self.size.y > other.position.y)





#position
#hitbox
#collision (self, other)
#update (zeit seid dem letzten Serverupdate)
#description

