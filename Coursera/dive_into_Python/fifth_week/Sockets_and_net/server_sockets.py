# Socket creating, server

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 10001))  # max port 65535
sock.listen(socket.SOMAXCONN)
# .listen has non obligatory parameter "backlog"
# which load all unregister data(which not invoked accept method) into backlog
# if the data overloads the amount - raise ConnectionRefused

connection, address = sock.accept()  # start receiving income connection // is blocked until receive a connection
# when a client sends us <connect> method - accept returns full duplex channel object
# this object has methods for reading and writing data to/from the channel
while True:
    # we are reading from our full duplex channel
    data = connection.recv(1024)
    # if there is no data - we terminate the loop execution and close socket and connection
    if not data:
        break
    # process data
    print(data.decode("utf8"))

connection.close()
sock.close()