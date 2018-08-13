from server.gameobject import gameobject
from Vector import Vector

class Meadow (gameobject):
    def __init__(self, position, size, description=""):
        super(Meadow, self).__init__(self, position, False, 0, size, Vector(), description)


