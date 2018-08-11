from time import sleep, time
import pygame
from pygame.locals import *
from time import time

from clientUser.Communication import Communication
from clientUser.ViewWindow import ViewWindow

tobiasIP = "192.168.2.106"
martinIP = "192.168.2.102"


if __name__ == "__main__":
    print("client")

    def handle_message(target, request, **content):
        if target == 'root':
            if request == 'test':
                print("test-message: " + str(content['value']))
        elif target == 'view_window':
            vew_window.handle(request, **content)

    def update_everything():
        pass

    pygame.init()

    # visual init
    vew_window = ViewWindow()
    vew_window.set_display(pygame)

    # communication init
    com = Communication(tobiasIP, 7694)
    com.connect()

    clock = pygame.time.Clock()
    running = True
    epoch = time()
    frame_count = 0
    while running:
        # server events
        while com.has_next():
            message = com.pop()
            handle_message(**message)

        # client events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                running = False

        if running:
            clock.tick(100)
            frame_count += 1
            if time() - epoch > 10:
                print("{} fps".format(round(frame_count / (time() - epoch), 2)))
                epoch = time()
                frame_count = 0

            vew_window.clear()
            update_everything()
            vew_window.update(pygame)