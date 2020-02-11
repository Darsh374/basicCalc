import unittest

from MathOperations.addition import Addition
from MathOperations.subtraction import Subtraction


class MyTestCase(unittest.TestCase):

    def test_MathOperations_Addition(self):
        calculator = Calculator()
        calculator.Sum(1, 2)
        self.assertEqual(3, Addition.sum(1, 2))

    def test_calculator_return_difference(self):
        calculator = Calculator()
        calculator.Difference(1, 2)
        self.assertEqual(-1, result)

    def test_calculator_access_difference_result(self):
        calculator = Calculator()
        calculator.Difference(1, 2)
        self.assertEqual(-1, calculator.Result)

    def test_calculator_access_sum_result(self):
        calculator = Calcualtor()
        calculator.Sum(1, 2)
        self.assertEqual(3, calculator.Result)

    def test_calculator_multiply(self):
        calculator = Calculator()
        result = calculator.multiply(1, 2)
        self.assertEqual(2, result)

    def test_calculator_divide(self):
        calculator = Calculator()
        result = calculator.divide(6, 3)
        self.assertEqual(2, result)


if __name__ == '__main__':
    unittest.main()
