from clientUser.Communication import Communication
from time import sleep

tobiasIP = "192.168.2.106"
martinIP = "192.168.2.102"

if __name__ == "__main__":
    print("client")
    com = Communication("localhost", 7694)
    com.connect()
    while True:
        com.send(b'abc\n')
        sleep(4)