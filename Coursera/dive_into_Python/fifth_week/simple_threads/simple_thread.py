# Thread creating

from threading import Thread


def func(name):
    print("hello", name)


th = Thread(target=func, args=("Oleh",))  # Passing the func and args list for execution in a thread
th.start()  # Start executing of our thread
th.join()  # Waiting for executing of the thread and terminates

