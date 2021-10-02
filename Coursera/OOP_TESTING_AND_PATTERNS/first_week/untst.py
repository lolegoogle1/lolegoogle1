import unittest


# =============== Test object ==============
def fib(n: int) -> int:
    """
    Calculates fibonacci number by it's index
    """
    pass


# ============= Test =======================
class TestFibonacciNumbers(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(fib(0), 0)

    def test_simple(self):
        for n, fib_n in (1, 1), (2, 1), (3, 2), \
                        (4, 3), (5, 5):
            with self.subTest(i=n):
                self.assertEqual(fib(n), fib_n)

    def test_positive(self):
        self.assertEqual(fib(10), 55)
