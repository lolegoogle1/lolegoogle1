# Creating process with <os.fork>

import time
import os

pid = os.fork()
print(pid)
if pid == 0:
    # child process
    while True:
        print("child: ", os.getpid())
        time.sleep(5)
else:
    # parent process
    print("parent: ", os.getpid())
    os.wait()  # an additional system call, which gives us time till a child process is completed

# =========== Hierarchical view of the process ======================
# ps axf | grep parent_child.py

# ===========          Strace                  ======================
# $ sudo strace -p parent_process_pid
# output> strace: Process parent_pid_process attached wait4(-1,
# $ sudo strace -p child_process_pid
# >getpid()                                = 8074
# >write(1, "child: ", 7)                  = 7
# >write(1, " ", 1)                        = 1
# >write(1, "8074", 4)                     = 4
# >write(1, "\n", 1)                       = 1
# >select(0, NULL, NULL, NULL, {tv_sec=5, tv_usec=0}) = 0 (Timeout)


