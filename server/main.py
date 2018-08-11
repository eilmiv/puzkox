from server.Communication import Communication
from time import sleep

if __name__ == "__main__":
    print("server")

    com = Communication(7694)
    com.start()
    while True:
        for client in com.clients:
            while client.has_message():
                message = client.pop()
                if message['request'] == 'test':
                    print("test-message: " + str(message['value']))
                if message ['target'] == "client":
                    client.handle_event(**message)
                if message ["target"] == "key_down":
                    client.handle_event(**message)
                if message["target"] == "root":
                    client.handle_event(**message)

        if len(com.clients)>0:
            client1 = com.clients[0]
            client1.send_coordinates()
            client1.flush()

