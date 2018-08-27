from Vector import Vector
from server.Chunk import Chunk
from time import time


class Map:
    def __init__(self):
        width = 10
        height = 10
        self.rows = []
        for x in range(width):
            self.rows.append([])
            for y in range(height):
                self.rows[-1].append(Chunk(Vector(x, y)))
        self.game_objects_slow = []
        self.game_objects = []
        self.time_fast = time()
        self.time_slow = time()

    def update(self):
        delta = time() - self.time_fast
        self.time_fast = time()
        self.update_cycle(self.game_objects, delta)
        self.game_objects = filter(lambda obj:obj.updating, self.game_objects)

    def update_slow(self):
        delta = time() - self.time_slow
        self.time_slow = time()
        self.update_cycle(self.game_objects_slow, delta)
        self.game_objects_slow = filter(lambda obj: obj.updating, self.game_objects_slow)

    def update_cycle(self, object_list, delta):
        for game_object in object_list:
            game_object.move(delta)
            x = round(game_object.position.x)
            y = round(game_object.position.y)
            chunk = self.rows[x][y]
            chunk.transfer(game_object)

        for game_object in object_list:
            colliding = []
            for ix in (x + i for i in range(-1, 2) if 0 <= x + i < len(self.rows)):
                row = self.rows[ix]
                for iy in (y + j for j in range(-1, 2) if 0 <= y + j < len(row)):
                    chunk = row[iy]
                    colliding.extend(obj for obj in chunk.content if obj.colliding(game_object))
            game_object.update(colliding)
            if not game_object.exist:
                game_object.updating = False

    def handle(self):
        pass
