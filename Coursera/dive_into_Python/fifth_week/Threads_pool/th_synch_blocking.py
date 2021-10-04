# Threads synch, blocking

import threading

# Creating the mutex objects
a = threading.RLock()
b = threading.RLock()

# An example of bad mutex objects use. The sequence of the acquiring and releasing is wrong.
# It leads to DEADLOCK
"""def foo():
    try:
        # Acquiring of the block, without context manager
        a.acquire()
        b.acquire()
    finally:
        # Releasing the block without context manager
        a.release()
        b.release()"""