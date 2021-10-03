# Parent and child files

# cat data.txt
# example string1
# example string2

import os

f = open("t_files/data.txt")
foo = f.readline()
print(foo)

if os.fork() == 0:
    # Child process
    foo = f.readline()
    print("child:", foo)
else:
    # Parent process
    foo = f.readline()
    print("parent:", foo)
