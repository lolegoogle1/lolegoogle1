# Several connections processing in the same time
import socket
import threading


def process_request(conn, addr):
    print("connected client:", addr)
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data.decode("utf8"))


with socket.socket() as sock:
    sock.bind(("", 10001))  # bind to localhost, 10001 port
    sock.listen()  # listening for new connections
    while True:
        conn, addr = sock.accept()  # receiving connection
        th = threading.Thread(target=process_request,
                              args=(conn, addr))  # put the func processing of the connection into the thread
        th.start()  # starting our thread with the func to process