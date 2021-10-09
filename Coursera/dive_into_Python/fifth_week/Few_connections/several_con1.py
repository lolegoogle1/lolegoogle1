# Several connections processing in the same time
import socket
import threading
import multiprocessing
import os


def worker(sock):
    while True:
        connection, address = sock.accept()
        print("pid", os.getpid())
        th = threading.Thread(target=process_request,
                              args=(connection, address))
        th.start()


def process_request(conn, addr):
    print("Connected client:", addr)
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data.decode("utf9"))


with socket.socket() as sock:
    sock.bind(("", 10001))
    sock.listen()

    workers_count = 3
    workers_list = [multiprocessing.Process(target=worker,
                                            args=(sock,))
                    for _ in range(workers_count)]

    for w in workers_list:
        w.start()

    for w in workers_list:
        w.join()
