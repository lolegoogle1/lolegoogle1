# PEP 0380, generators and coroutines

def chain(x_iterable, y_iterable):
    yield from x_iterable
    print("123123123")
    yield from y_iterable


# The same function shows how exactly function works above
def the_same_chain(x_iterable, y_iterable):
    for x in x_iterable:
        yield x

    for y in y_iterable:
        yield y


a = [1, 2, 3]  # Iterable object
b = (4, 5)  # Iterable object
for x in chain(a, b):
    print(x)