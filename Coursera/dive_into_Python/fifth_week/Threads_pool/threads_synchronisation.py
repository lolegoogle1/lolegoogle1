# Queues, <queue> module
from queue import Queue
from threading import Thread


def worker(q, n):
    while True:
        item = q.get()
        if item is None:
            break
        print("process data:", n, item)


# If there is more than declared amount of the places in the queue -
# the thread should be blocked until a free place is available
q = Queue(5)
# Create a few threads to proceed with our queue elements
th1 = Thread(target=worker, args=(q, 1))  # pass <worker> func, which works with our queue
th2 = Thread(target=worker, args=(q, 2))
th1.start()  # Start executing of our thread
th2.start()

for i in range(50):
    q.put(i)

q.put(None)
q.put(None)

th1.join()  # Waiting for executing of the thread and terminates
th2.join()

