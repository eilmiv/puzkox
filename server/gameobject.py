import Vector
import server.options as optoins


class GameObject:
    def __init__(self, position, description=""):
        self.position = position
        self.description = description
        self.exist = True
        self.updating = True
        self.current_chunk = None
        self.id = optoins.gameobject_count
        optoins.gameobject_count += 1

    def delete_from_chunk(self):
        if self.current_chunk and self in self.current_chunk.content:
            self.current_chunk.content.remove(self)



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

    def no_partition_edge(self, other):
        for support_vector, normal_vector in self.edges():
            dividing = True
            for vertex in other.vertices():
                if (vertex - support_vector) * normal_vector < 0:
                    dividing = False
                    break
            if dividing:
                return False
        return True

    def colliding(self, other):
        return self.no_partition_edge(other) and other.no_partition_edge(self)

    def move(self, delta_t):
        pass

    def update(self, colliding):
        self.updating = False

    def serialize(self):
        print("ACchtung !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return {}

#position
#hitbox
#collision (self, other)
#update (zeit seid dem letzten Serverupdate)
#description

