import time


class Timer:
    def __init__(self):
        self.start = time.time()

    def __call__(self, func):
        def wrapped(*args, **kwargs):
            print("we are calculating the time")
            func(*args, **kwargs)
            print("Elapsed time: {}".format(time.time() - self.start))
            return
        return wrapped()


timer = Timer()


@timer
def wasting_time_func():
    time.sleep(5)


"""class timer():
    def __init__(self):
        self.start = time.time()

    def current_time(self):
        return time.time() - self.start

    def __enter__(self):
        return self

    def __exit__(self, *args):
        print("Elapsed: {}".format(self.current_time()))


with timer() as t:
    time.sleep(1)
    print('Current: {}'.format(t.current_time()))
    time.sleep(1)"""