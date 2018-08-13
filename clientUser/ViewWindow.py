from clientUser.Commander import Commander
from Vector import Vector


class ViewWindow(Commander):
    def __init__(self):
        super(ViewWindow, self).__init__()
        self.location = Vector()
        self.game_size = Vector(5, 5)
        self.width = 500
        self.height = 300
        self.display = None
        self.pygame = None
        self.font = None

    def handle(self, request, **content):
        if request == "update":
            key = content['key']
            if key == 'location':
                self.location = Vector(content['x'], content['y'])

    def get_size(self):
        return self.width, self.height

    def set_size(self, size):
        self.width, self.height = size

    def set_display(self, pygame):
        #pygame.FULLSCREEN
        self.display = pygame.display.set_mode(self.get_size(), pygame.DOUBLEBUF | pygame.RESIZABLE)
        pygame.display.set_caption("Puzkox")
        self.pygame = pygame
        self.font = pygame.font.SysFont(pygame.font.get_default_font(), 20)

    def resize(self, size):
        self.set_size(size)
        self.add('client', 'size', width=self.width, height=self.height)
        if self.pygame:
            self.display = self.pygame.display.set_mode(self.get_size(), self.pygame.DOUBLEBUF | self.pygame.RESIZABLE)

    def clear(self):
        self.display.fill((255, 0, 255))

    def update(self, pygame):
        pygame.display.update()

    def screen_coordinates(self, vec):
        res = Vector(vec.x / self.game_size.x * self.width, vec.y / self.game_size.y * self.height)
        return res

    def draw_image(self, image, pos):
        rect = image.get_rect()
        rect.center = self.screen_coordinates(pos-self.location).tuple()
        self.display.blit(image, rect)

    def status_text(self, text):
        if self.font:
            width, height = self.font.size(text)
            posY = 2
            for line in text.splitlines():
                self.display.blit(self.font.render(line, False, (0, 0, 0)), (2, posY))
                posY += height + 3