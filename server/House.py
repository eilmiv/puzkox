from server.Square import Square
from time import time
import server.options as options


class House(Square):
    def __init__(self, position, site_length=1, description="House"):
        super(House, self).__init__(position, site_length, description)
        self.last_hit = 0

    def serialize(self):
        damage = 0
        time_diff = time() - self.last_hit
        if time_diff <= options.time_house:
            damage = 1 - time_diff/options.time_house
        return {"location_x":self.position.x, "location_y":self.position.y, "texture":"house", "damage":damage}

