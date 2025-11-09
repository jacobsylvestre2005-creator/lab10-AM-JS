# https://github.com/jacobsylvestre2005-creator/lab10-AM-JS
# Partner 1: Jacob Sylvestre
# Partner 2: Avi McCarthy 

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


    def test_multiply(self):
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(0, 100), 0)

    def test_divide(self):
        self.assertAlmostEqual(div(2, 10), 5) 
        self.assertAlmostEqual(div(5, 25), 5)  
        self.assertAlmostEqual(div(-4, 8), -2) 

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
            
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            log(-5, 10)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(-3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(0, 0), 0.0)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(9), 3.0)
        self.assertAlmostEqual(square_root(0), 0.0)
        with self.assertRaises(ValueError):
            square_root(-9)

# Do not touch this
if __name__ == "__main__":
    unittest.main()