from Vector import Vector


class GameObject:
    def __init__(self, location=Vector(), angle=0, texture='none', version=0, biome=0, damage=0,
                 directions={'north': False, 'east': False, 'south': False, 'west': False}, **dummy):
        self.location = location
        self.angle = angle
        self.texture = texture
        self.version = version
        self.biome = biome
        self.damage = damage
        self.directions = directions
