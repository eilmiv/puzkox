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






#position
#hitbox
#collision (self, other)
#update (zeit seid dem letzten Serverupdate)
#description

