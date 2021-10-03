# Creating of a thread with classes

from threading import Thread


class PrintThread(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self) -> None:  # Override method run for running in a thread
        print("hello", self.name)


th = PrintThread("Oleh")  # Passing the args list for execution in a thread class
th.start()  # Start executing of the thread
th.join()  # Waiting for the response about the finish of executing the thread
