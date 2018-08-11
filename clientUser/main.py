import pygame
from pygame.locals import *
from time import time

from clientUser.Communication import Communication
from clientUser.ViewWindow import ViewWindow

tobiasIP = "192.168.2.106"
martinIP = "192.168.2.102"

useIP = "localhost"

if __name__ == "__main__":
    print("client")

    def handle_message(target, request, **content):
        if target == 'root':
            if request == 'test':
                print("test-message: " + str(content['value']))
            elif request == 'ping-answer':
                print("ping: {}".format(int((time() - content['time'])*1000)))
        elif target == 'view_window':
            vew_window.handle(request, **content)

    def update_everything():
        pass

    def handle_key(key):
        v = ''
        if key == 'w':
            v = 'forward'
        elif key == 'a':
            v = 'left'
        elif key == 's':
            v = 'backward'
        elif key == 'd':
            v = 'right'

        if v:
            com.send('client', 'key_down', value=v)

    pygame.init()
    commanders = []

    # visual init
    vew_window = ViewWindow()
    vew_window.set_display(pygame)
    commanders.append(vew_window)

    # communication init
    com = Communication(useIP, 7694)
    com.connect()
    com.send('client', 'size', width=vew_window.width, height=vew_window.height)
    com.flush()

    clock = pygame.time.Clock()
    running = True
    epoch = time()
    frame_count = 0
    com.send('root', 'ping', time=time())
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
            elif event.type == VIDEORESIZE:
                vew_window.resize(event.dict['size'], pygame)
            elif event.type == KEYDOWN:
                handle_key(event.dict['unicode'])

        # send messages
        for commander in commanders:
            commander.send(com)
        com.flush()

        if running:
            clock.tick(100)
            frame_count += 1
            if time() - epoch > 10:
                print("{} fps".format(round(frame_count / (time() - epoch), 2)))
                epoch = time()
                frame_count = 0
                com.send('root', 'ping', time=time())


            vew_window.clear()
            update_everything()
            vew_window.update(pygame)