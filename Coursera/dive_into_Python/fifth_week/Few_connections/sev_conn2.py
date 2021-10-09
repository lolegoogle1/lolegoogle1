# Nonblocking IO, example

import socket
import select

sock = socket.socket()
sock.bind(("", 10001))
sock.listen()

conn1, addr = sock.accept()
conn2, addr = sock.accept()

# the same as <settimeout(0)> and if there is no data - method returns error about it
conn1.setblocking(0)
conn1.setblocking(0)

# Object epoll
epoll = select.epoll()
# Register in our epoll objects file descriptors for each connection, mask for input and output
epoll.register(conn1.fileno(), select.EPOLLIN | select.EPOLLOUT)
epoll.register(conn2.fileno(), select.EPOLLIN | select.EPOLLOUT)

# dict with file descriptors as keys, and connection objects as value
conn_map = {
    conn1.fileno(): conn1,
    conn2.fileno(): conn2,
}

# Event loop of events in epoll

while True:
    events = epoll.poll(1)
    # system call which returns list of events
    # it contains a file descriptor and event(events which have happen with the descriptor)
    for fileno, event in events:
        # We should check what kind of event has been returned
        # and with the information - take some proper actions

        # if socket is ready for sending data
        if event & select.EPOLLIN:
            data = conn_map[fileno].recv(1024)
            print(data.decode("utf8"))
        # if socket is ready to receive some data
        elif event & select.EPOLLOUT:
            conn_map[fileno].send('ping'.encode("utf8"))
