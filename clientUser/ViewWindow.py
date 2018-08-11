from clientUser.Commander import Commander
from Vector import Vector


class ViewWindow(Commander):
    def __init__(self):
        super(ViewWindow, self).__init__()
        self.location = Vector()
        self.width = 500
        self.height = 300
        self.display = None

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

    def resize(self, size, pygame):
        self.set_size(size)
        self.add('client', 'size', width=self.width, height=self.height)
        self.display = pygame.display.set_mode(self.get_size(), pygame.DOUBLEBUF | pygame.RESIZABLE)

    def clear(self):
        self.display.fill((255, 255, 255))

    def update(self, pygame):
        pygame.display.update()