from Vector import Vector


class GameObject:
    def __init__(self, location_x=0, location_y=0, angle=0, texture='none', version=0, biome=0, damage=0,
                 directions={'north': False, 'east': False, 'south': False, 'west': False}, foreground=False, **dummy):
        self.location = Vector(location_x, location_y)
        self.angle = angle
        self.texture = texture
        self.version = version
        self.biome = biome
        self.damage = damage
        self.directions = directions
        self.foreground = foreground
