"""Custom context manager example"""


class open_file:
    def __init__(self, filename, mode):
        self.f = open(filename, mode)

    def __enter__(self):
        return self.f

    def __exit__(self, *args):
        self.f.close()


with open_file('../test.log', 'w') as f:
    f.write('Inside "open_file" context manager')

with open_file('../test.log', 'r') as f:
    print(f.readlines())

