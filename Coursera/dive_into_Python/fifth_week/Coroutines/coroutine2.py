# Couroutines, close() method

def grep(pattern):
    print("start grep")
    try:
        while True:
            line = yield
            if pattern in line:
                print(line)
    except GeneratorExit:
        print("stop grep")


coroutine = grep("python")
next(coroutine)

coroutine.send("python is the best!")
coroutine.throw(RuntimeError)
coroutine.close()