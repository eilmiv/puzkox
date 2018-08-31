from Vector import Vector


class Chunk:
    def __init__(self, location):
        self.location = location
        self.content = []

    def remove(self, obj):
        if obj in self.content:
            self.content.remove(obj)

    def transfer(self, obj):
        if obj.current_chunk != self:
            if obj.current_chunk:
                obj.current_chunk.remove(obj)
            self.content.append(obj)
            obj.current_chunk = self
