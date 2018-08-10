from Vector import Vector
class Player:
    def __init__(self):
        self.possition = Vector()
        self.health = 0
        self.energy = 0
        self.charges = 0

    def serealize (self):
        return "{}!{}!{}!{}".format(self.possition.x,self.possition.y, self.health, self.energy, self.charges)


