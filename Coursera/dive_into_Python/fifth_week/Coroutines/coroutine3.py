# Coroutine calls, PEP 380

def grep(pattern):
    print("start grep")
    while True:
        line = yield
        if pattern in line:
            print(line)


def grep_python_coroutine():
    g = grep("python")
    yield from g


g = grep_python_coroutine()  # coroutine, because of yield from

g.send(None)  # for the start of the coroutine
g.send("python is awesome language!")