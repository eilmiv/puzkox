class Player:
    def __init__(self, position, health, energy, charges):
        self.position = position
        self.health = health
        self.energy = energy
        self.charges = charges

    def __repr__(self):
        return "Player at {}, ".format(self.position)
