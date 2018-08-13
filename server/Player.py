from Vector import Vector
from server.gameobject import gameobject


class Player (gameobject):
    def __init__(self, position, is_circle, angle, size, offset, description):
        super(Player, self).__init__(self, position, is_circle, angle, size, offset, description)
        self.health = 0
        self.energy = 0
        self.charges = 0

    def serealize (self):
        return "{}!{}!{}!{}".format(self.possition.x,self.possition.y, self.health, self.energy, self.charges)

    def update(self):
        pass

if __name__ == "__main__":
    print("hi")
