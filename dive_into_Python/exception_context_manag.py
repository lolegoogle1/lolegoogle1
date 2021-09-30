"""EXception context manager example // contextlib analogue"""


class suppress_exception:
    def __init__(self, exc_type):
        self.exc_type = exc_type

    def __enter__(self):
        return

    def __exit__(self, exc_type, exc_val, exc_traceback):
        if exc_type == self.exc_type:
            print('Nothing happend.')
            return True


with suppress_exception(ZeroDivisionError):
    really_big_number = 1 / 0
