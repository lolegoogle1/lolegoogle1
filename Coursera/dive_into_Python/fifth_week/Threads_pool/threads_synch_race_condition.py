# Threads synch, race condition

import threading


class Point(object):
    def __init__(self, x, y):
        # Creating the block object
        self.mutex = threading.RLock()
        self.set(x, y)

    def get(self):
        # while entering the context manager - acquire the mutex
        # while exiting - releasing
        # can be done many times,
        # but there should be 1 release for each current acquire before the next acquirement
        with self.mutex:
            return (self.x, self.y)

    def set(self, x, y):
        # while entering the context manager - acquire the mutex
        # while exiting - releasing
        # can be done many times,
        # but there should be 1 release for each current acquire before the next acquirement
        with self.mutex:
            self.x = x
            self.y = y


# use in threads
my_point = Point(10, 20)
my_point.set(15, 10)
print(my_point.get())
