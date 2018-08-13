from server.Communication import Communication
from time import sleep, time
import pygame
from server import Player
import Vector

if __name__ == "__main__":
    print("server")

    com = Communication(7694)
    com.start()

    Uhr = pygame.time.Clock()

    frame_count = 0
    epoch=time()
    while True:

        frame_count +=1
        if time() - epoch > 10:
            server_fps = int(frame_count / (time() - epoch))
            com.send_all("root", "server-fps", fps=server_fps)
            frame_count = 0
            epoch = time()

        for client in com.clients:
            if client.player is None:
                Player(Vector(), False, 0, )

            while client.has_message():
                message = client.pop()
                if message['request'] == 'test':
                    print("test-message: " + str(message['value']))
                if message ['target'] == "client":
                    client.handle_event(**message)
                if message["target"] == "root":
                    client.handle_event(**message)

        for client in com.clients:
            client.send_coordinates()
            client.flush()
        Uhr.tick(120)


