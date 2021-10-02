class Class:
    __slots__ = ['dart_veider']

    def __init__(self):
        self.dart_veider


obj = Class()

obj.luke = 'the chosen too'


# Traceback (most recent call last):
# File "C:\Users\Oleh Hryshchuk\PycharmProjects\first_step\Coursera\dive_into_Python\fourth_week\descriptors\slots_example.py", line 8, in <module>
#   obj = Class()
# File "C:\Users\Oleh Hryshchuk\PycharmProjects\first_step\Coursera\dive_into_Python\fourth_week\descriptors\slots_example.py", line 5, in __init__
#   self.dart_veider
# AttributeError: dart_veider
