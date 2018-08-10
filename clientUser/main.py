from Communication import Communication
from time import sleep

if __name__ == "__main__":
    print("client")
    com = Communication("192.168.2.106", 7694)
    com.connect()
    while True:
        sleep(10)