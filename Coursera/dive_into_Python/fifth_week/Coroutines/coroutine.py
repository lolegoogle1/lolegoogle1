# Coroutines

def grep(pattern):
    print("start grep")
    while True:
        line = yield  # we assign the result of the yield func to the variable "line"
        if pattern in line:
            print(line)
        else:
            print("This doesn't fit!")


grep_coroutine = grep("python")
next(grep_coroutine)  # grep_generator.send(None) - start of the generator/coroutine
while True:
    var = input("Enter your value: ")
    if not var:
        break
    grep_coroutine.send(var)
