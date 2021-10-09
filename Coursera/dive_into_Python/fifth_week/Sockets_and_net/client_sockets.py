# Creating sockets, client

import socket

sock = socket.socket()  # Thread socket, AF_INET family
sock.connect(("127.0.0.1", 10001))  # is blocked until server would not invoke <accept> method
# after that - socket is ready to work
sock.sendall("ping".encode("utf8"))  # <send> <sendall> <recv> methods are available
sock.close()  # close our socket


# Shorter record of the same
'''
    sock = socket.create_connection("127.0.0.1", 10001))
    sock.sendall("ping".encode("utf8"))
    sock.close()
'''