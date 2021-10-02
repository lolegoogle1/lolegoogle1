from abc import ABCMeta, abstractmethod


class Sender(metaclass=ABCMeta):
    @abstractmethod
    def send(self):
        """Do something"""
        pass


class Child(Sender):
    def send(self):
        print('Sending')


print(Child())

# ============================  Code    ======================================
"""from abc import ABCMeta, abstractmethod


class Sender(metaclass=ABCMeta):
    @abstractmethod
    def send(self):
        '''Do something'''
        pass


class Child(Sender):
    pass


Child()"""
# ============================ Response ======================================
"""
 There is type error bcs, we have no obligatory abstract method inside the Child class
 TypeError: Can't instantiate abstract class Child with abstract method <send>"""
