from server.Communication import Communication
from time import sleep

if __name__ == "__main__":
    print("server")

    com = Communication(7694)
    com.start()
    while True:
        print("hi")
        for client in com.clients:
            while client.has_message():
                message = client.pop()
                if message['type'] == 'test':
                    print("test-message: " + str(message['value']))
        sleep(2)