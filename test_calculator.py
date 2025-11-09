import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self):
        assert add(5, 5) == 10
        assert add(100, 56) == 156
        assert add(12, 82) == 94

    def test_subtract(self):
        assert sub(5, 5) == 0
        assert sub(100, 56) == 44
        assert sub(12, 82) == -70

    def test_divide_by_zero(self):
       with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        assert log(5, 5) == 1
        assert log(2, 8) == 3
        assert log(5, 625) == 4

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(1, 0)

# Do not touch this
if __name__ == "__main__":
    unittest.main()