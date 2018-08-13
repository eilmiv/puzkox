from Vector import Vector
from clientUser.GameObject import GameObject


class GameScene:
    def __init__(self, canvas, images):
        self.canvas = canvas
        self.images = images
        self.game_objects = {}

    def update(self):
        for game_object in self.game_objects.values:
            texture = game_object.texture
            if texture == 'car':
                self.canvas.draw_image(self.images.get_car(game_object.angle, game_object.version, game_object.damage),
                                       game_object.location)
            elif texture == 'grass':
                self.canvas.draw_image(self.images.get_grass(game_object.biome, game_object.version),
                                       game_object.location)
            elif texture == 'house':
                self.canvas.draw_image(self.images.get_house(game_object.biome, game_object.version, game_object.damage),
                                       game_object.location)
            elif texture == 'street':
                self.canvas.draw_image(self.images.get_street(game_object.biome, game_object.version, game_object.directions),
                                       game_object.location)

    def handle(self, request, **content):
        if request == 'update':
            id = content['id']
            key = content['key']
            if key == 'location':
                self.game_objects[id].location = Vector(content['x'], content['y'])
            elif key == 'damage':
                self.game_objects[id].damage = content['value']
            elif key == 'texture':
                self.game_objects[id].texture = content['texture']
        elif request == 'create':
            self.game_objects[content[id]] = GameObject(**content)
