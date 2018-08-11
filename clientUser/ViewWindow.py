from Vector import Vector


class ViewWindow:
    def __init__(self):
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

    def set_display(self, pygame):
        self.display = pygame.display.set_mode(self.get_size())
        pygame.display.set_caption("Puzkox")

    def clear(self):
        self.display.fill((255, 255, 255))

    def update(self, pygame):
        pygame.display.update()


def init():
    pygame.init()