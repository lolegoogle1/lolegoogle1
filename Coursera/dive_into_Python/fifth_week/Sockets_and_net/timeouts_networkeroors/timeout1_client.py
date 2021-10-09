# socket creating, timeouts and error handling
# client
import socket

with socket.create_connection(("127.0.0.1", 10001), 5) as sock:
    # connect timeout(5sec) - only for establishing connection to the server
    # set socket read timeout
    sock.settimeout(2)  # timeout for any operation with our socket
    try:
        sock.sendall("ping".encode("utf8"))
    except socket.timeout:
        print("send data timeout")
    except socket.error as ex:
        print("send data error", ex)