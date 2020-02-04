import unittest

from MathOperations.addition import Addition
from MathOperations.subtraction import Subtraction


class MyTestCase(unittest.TestCase):

    def test_MathOperations_Addition(self):
        calculator = Calculator()
        result = calcualtor.Sum(1, 2)
        self.assertEqual(3, Addition.sum(1, 2))

    def test_calculator_subtraction(self):
        calculator = Calculator()
        result = calcualtor.(1, 2)
        self.assertEqual(-1, Subtraction.difference(1, 2))

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
