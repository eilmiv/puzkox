from server.Communication import Communication
from time import sleep, time
import pygame
from server import Player
import Vector
from server.Map import Map

if __name__ == "__main__":
    print("server")

    com = Communication(7694)
    com.start()

    Uhr = pygame.time.Clock()
    world = Map()

    frame_count = 0
    epoch=time()
    while True:
        delta = Uhr.tick(120)

        frame_count +=1
        if time() - epoch > 10:
            server_fps = int(frame_count / (time() - epoch))
            com.send_all("root", "server-fps", fps=server_fps)
            frame_count = 0
            epoch = time()

        # receaving and player init
        for client in com.clients:
            if client.player is None:
                client.player = Player(Vector(), 0)
                client.player.client = client
                world.add(client.player)

            while client.has_message():
                message = client.pop()
                if message['request'] == 'test':
                    print("test-message: " + str(message['value']))
                if message ['target'] == "client":
                    client.handle_event(**message)
                if message["target"] == "root":
                    client.handle_event(**message)

        world.update(delta)

        # update clients
        for client in com.clients:
            world.update_client(client, delta)

        # sending
        for client in com.clients:
            client.send_coordinates()
            client.flush()
