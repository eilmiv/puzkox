import Vector


class GameObject:
    def __init__(self, position, description=""):
        self._position = position
        self.description = description

    @property
    def position(self):
        return self._position

    @position.setter
    def set_position (self, new_position):
        self._position = new_position

    def vertices(self):
        return []

    def edges(self):
        vertices = list(self.vertices())
        if len(vertices) > 0:
            last = vertices[-1]
            for vertex in vertices:
                yield vertex, (last - vertex).rotate90()
                last = vertex
        else:
            return

    def colliding(self, other):
        for support_vector, normal_vector in self.edges():
            dividing = True
            for vertex in other.vertices():
                if (vertex - support_vector) * normal_vector < 0:
                    dividing = False
                    break
            if dividing:
                return False
        return True


#position
#hitbox
#collision (self, other)
#update (zeit seid dem letzten Serverupdate)
#description

