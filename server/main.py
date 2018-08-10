from server.Communication import Communication, CommunicationAlt
from time import sleep

if __name__ == "__main__":
    print("server")

    com = CommunicationAlt(7694)
    com.start()
    while True:
        com.update()
        print("hi")
        sleep(2)