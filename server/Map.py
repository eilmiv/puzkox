from Vector import Vector
from server.Chunk import Chunk
from time import time
import math


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
        self.time_slow = time()

    def update(self, delta):
        self.update_cycle(self.game_objects, delta / 1000)
        self.game_objects = filter(lambda obj: obj.updating, self.game_objects)

    def update_slow(self):
        delta = time() - self.time_slow
        self.time_slow = time()
        self.update_cycle(self.game_objects_slow, delta)
        self.game_objects_slow = filter(lambda obj: obj.updating, self.game_objects_slow)

    def update_cycle(self, object_list, delta):
        for game_object in object_list:
            game_object.move(delta)
            x, y = self.update_chunk(game_object)

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

    def add(self, obj):
        if obj not in self.game_objects:
            self.game_objects.append(obj)
            self.update_chunk(obj)

    def update_chunk(self, game_object):
        x = round(game_object.position.x)
        y = round(game_object.position.y)
        chunk = self.rows[x][y]
        chunk.transfer(game_object)
        return x, y

    def handle(self):
        pass

    def update_client(self, client, delta):
        x1 = math.floor(client.position.x)
        y1 = math.floor(client.position.y)
        x2 = math.ceil(client.position.x + client.size.x)
        y2 = math.ceil(client.position.y + client.size.y)
        colliding = []
        for row in (self.rows[x] for x in range(x1, x2+1) if 0 <= x < len(self.rows)):
            for chunk in (row[y] for y in range(y1, y2+1) if 0 <= y < len(row)):
                colliding.extend(chunk.content)
        client.update(colliding, delta)
