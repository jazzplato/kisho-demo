import time
import socket
from contextlib import closing

SLEEP_TIME = 5
HOST_MYSQL = "kisho-mysql"
HOST_REDIS = "kisho-redis"
PORT_MYSQL = 3306
PORT_REDIS = 6379


def check_socket(host, port):
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        return sock.connect_ex((host, port)) == 0


def main():
    while not check_socket(HOST_MYSQL, PORT_MYSQL):
        time.sleep(SLEEP_TIME)
    while not check_socket(HOST_REDIS, PORT_REDIS):
        time.sleep(SLEEP_TIME)
    print("ready to start")


if __name__ == "__main__":
    main()