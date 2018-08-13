from server.Square import Square
from Vector import Vector

class Meadow (Square):
    def __init__(self, position, size, description=""):
        super(Meadow, self).__init__(self, position, False, 0, size, Vector(), description)


