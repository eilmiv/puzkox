from server.Square import Square
from Vector import Vector


class Meadow (Square):
    def __init__(self, position, site_length=1, description="Meadow"):
        super(Meadow, self).__init__(position, site_length, description)


