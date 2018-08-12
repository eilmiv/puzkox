import pygame
from pygame.locals import *
from time import time

from clientUser.Communication import Communication
from clientUser.ViewWindow import ViewWindow
from clientUser.GameScene import GameScene
from clientUser.ImageProvider import ImageProvider

tobiasIP = "192.168.2.106"
martinIP = "192.168.2.102"

useIP = "localhost"

if __name__ == "__main__":
    print("client")

    def handle_message(target, request, **content):
        global ping
        if target == 'root':
            if request == 'test':
                print("test-message: " + str(content['value']))
            elif request == 'ping-answer':
                ping = "ping: {}".format(int((time() - content['time'])*1000))
        elif target == 'view_window':
            vew_window.handle(request, **content)

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

    # basic init
    pygame.init()
    pygame.font.init()
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

    # scene state init
    images = ImageProvider(pygame, "Images")
    scene = GameScene(vew_window, images)
    print("car: " + str(images.car_images))
    print("grass: " + str(images.grass_images))
    print("house: " + str(images.house_images))
    print("street: " + str(images.street_images))
    print("biome report: {}".format(images.biome_report()))
    print("car report: {}".format(images.car_report()))

    # init timing
    clock = pygame.time.Clock()
    running = True
    epoch = time()
    frame_count = 0
    fps = ""
    ping = ""
    server_fps = ""
    com.send('root', 'ping', time=time())

    # main loop
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
                vew_window.resize(event.dict['size'])
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
                fps = "{} fps".format(round(frame_count / (time() - epoch), 2))
                epoch = time()
                frame_count = 0
                com.send('root', 'ping', time=time())
                print(vew_window.location)

            vew_window.clear()
            scene.update()
            vew_window.status_text("{}\n{}\n{}".format(fps, ping, server_fps))
            vew_window.update(pygame)