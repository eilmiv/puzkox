class GameScene:
    def __init__(self, canvas, images):
        self.canvas = canvas
        self.images = images
        self.test_image = canvas.pygame.image.load("Images/car_0_0.bmp")
        self.test_image = self.test_image.convert_alpha()

    def update(self):
        transformed = self.canvas.pygame.transform.scale(self.test_image, (128,128))
        transformed = self.canvas.pygame.transform.rotate(transformed, 60)

        self.canvas.draw_image(transformed)
