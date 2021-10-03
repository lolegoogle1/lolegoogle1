# Creating process, <multiprocessing> module

from multiprocessing import Process


class PrintProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    # Code for executing in the child process
    def run(self) -> None:
        print("hello", self.name)


p = PrintProcess("Mike")
p.start()
p.join()

