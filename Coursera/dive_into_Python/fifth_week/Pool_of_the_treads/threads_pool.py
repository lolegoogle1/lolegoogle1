# Threads pool, concurrent.futures.Future

from concurrent.futures import ThreadPoolExecutor, as_completed


def func(a):
    return a * a

# The needed amount of the threads will be created automatically
# .shutdown() in exit of the context manager execution


with ThreadPoolExecutor(max_workers=3) as pool:
    # max_workers - max amount of the threads to be created inside the 'with' statement
    results = [pool.submit(func, i) for i in range(10)]
    # the main purpose of the <submit> method. it creates the class object
    # Inside of the results we defined our sequence of the Future objects
    # concurrent.futures.Future is an object, that has not been finished, BUT is being processed and will be finished
    # as_completed - An iterator over the given futures that yields each as it completes.
    for future in as_completed(results):
        print(future.result())
