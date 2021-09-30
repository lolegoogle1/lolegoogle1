""" Here im going to test TDD concept with some examples """


from contracts import contract


#
# @contract(a='list', returns='list[N]')
def sort_algorithm(a):
    pass


def test_sort():
    print("Test #1")
    print('testcase ##1: ', end="")
    a = [4, 2, 5, 1, 3]
    a_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(a)
    passed = a == a_sorted
    print("OK" if passed else "FAIL")

    print("testcase ##2: ", end="")
    a = []
    a_sorted = []
    sort_algorithm(a)
    passed = a == a_sorted
    print("OK" if passed else "FAIL")

    print("testcase ##3: ", end="")
    a = [1, 2, 3, 4, 5]
    a_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(a)
    passed = a == a_sorted
    print("OK" if passed else "FAIL")


if __name__ == "__main__":
    test_sort()