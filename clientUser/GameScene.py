class GameScene:
    def __init__(self, canvas, images):
        self.canvas = canvas
        self.images = images

    def update(self):
        self.canvas.draw_image(self.images.get_street(north=True, east=True, south=True, west=True))
