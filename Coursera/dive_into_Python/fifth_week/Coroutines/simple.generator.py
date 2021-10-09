# Generator

def my_range_generator(top):
    current = 0
    print("Before loop\n")
    while current < top:
        print("Before yield")
        yield current
        print("after yield")
        current += 1


counter = my_range_generator(10)
print(counter)

for element in counter:
    print("Element:", element)
