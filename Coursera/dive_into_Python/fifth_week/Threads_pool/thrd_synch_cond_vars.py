# Threads synchronisation, condition vars
import threading


class Queue(object):
    def __init__(self, size=5):
        # max capacity of the queue
        self._size = size
        # defining queue
        self._queue = []
        # creating the mutex objects, for handling block process
        self._mutex = threading.RLock()
        # Creating conditions variables which give us an opportunity
        # to handle the condition of the queue
        self._empty = threading.Condition(self._mutex)
        self._full = threading.Condition(self._mutex)

    # Method for putting elements to the queue
    def put(self, val):
        # context manager with _full mutex
        with self._full:
            while len(self._queue) >= self._size:
                self._full.wait()  # waiting for a free place

            self._queue.append(val)  # append a new value to the queue
            self._empty.notify()  # Wake up one or more threads waiting on this condition, if any

    def get(self):
        with self._empty:
            while len(self._queue) == 0:
                self._empty.wait()

            ret = self._queue.pop(0) # release the element from the queue
            self._full.notify() # notify a/the thread/s about releasing the block
            return ret
