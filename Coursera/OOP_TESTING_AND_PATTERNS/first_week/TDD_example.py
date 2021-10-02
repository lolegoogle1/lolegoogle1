""" Here im going to test TDD concept with some examples """

from random import shuffle  # it randomizes order of elements


def sort_algorithm(a):
    """
    Sorting of list on place. Using Bubble Sort algorithm.
    """
    n = len(a)
    list_is_sorted = False
    bypass = 1
    while not list_is_sorted:
        list_is_sorted = True
        for k in range(n - bypass):
            if a[k] > a[k+1]:
                a[k], a[k+1] = a[k+1], a[k]
                list_is_sorted = False
        bypass += 1


def test_sort():
    print("Test #1")
    passed = True

    passed &= test_sort_works_in_simple_cases()
    passed &= test_sort_algorithm_stable()
    passed &= test_sort_algorithm_is_universal()
    passed &= test_sort_algorithm_scalability()

    print("Summary:", "Ok" if passed else "Fail")


def test_sort_works_in_simple_cases():
    print("- sort algorithm works in simple cases:", end=" ")
    passed = True

    for a1 in ([1], [], [1, 2], [1, 2, 3, 4, 5],
               [4, 2, 5, 1, 3], [5, 4, 4, 5, 5],
               list(range(20)), list(range(20, 1, -1))):
        a2 = sorted(list(a1))
        sort_algorithm(a1)
        passed &= all(x == y for x, y in zip(a1, a2))

    print("OK" if passed else "Fail")
    return passed


def test_sort_algorithm_stable():
    print("- sort algorithm is stable: ", end=" ")
    passed = True

    for a1 in ([[100] for i in range(5)],
               [[1, 2], [1, 2], [2, 2], [2, 2], [2, 3], [2, 3]],
               [[5, 2] for i in range(30)] + [[10, 5] for i in range(30)]):
        shuffle(a1)
        a2 = sorted(list(a1))
        sort_algorithm(a1)
        # to test stability i will check a1[i] not equals a2[i], but is a2[i]
        passed &= all(x is y for x, y in zip(a1, a2))

    print("OK" if passed else "Fail")
    return passed


def test_sort_algorithm_is_universal():
    print("- sort algorithm is universal:", end=" ")
    passed = True

    # testing types: str, float, list
    for a1 in (list('abcdefg'),
               [float(i) ** 0.5 for i in range(10)],
               [[1, 2], [2, 3], [3, 4], [3, 4, 5], [6, 7]]):
        shuffle(a1)
        a2 = sorted(list(a1))
        sort_algorithm(a1)
        passed &= all(x == y for x, y in zip(a1, a2))

    print("Ok" if passed else "Fail")
    return passed


def test_sort_algorithm_scalability(max_scale=100):
    print("- sort algorithm on scale={0}:".format(max_scale), end=" ")
    passed = True

    for a1 in (list(range(max_scale)),
               list(range(max_scale // 2, max_scale)) + list(range(max_scale // 2)),
               list(range(max_scale, 0, -1))):
        shuffle(a1)
        a2 = sorted(list(a1))
        sort_algorithm(a1)
        passed &= all(x == y for x, y in zip(a1, a2))

    print("Ok" if passed else "Fail")
    return passed


if __name__ == "__main__":
    test_sort()
