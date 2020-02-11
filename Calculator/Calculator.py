from MathOperations.addition import Addition

import math


class Calculator:
    Result = 0
    def __init__(self):
        pass

    def Sum(self, a, b):
        self.Result = Addition.sum(a, b)
        return self.Result

    def Difference(self, a, b):
        self.Result = Subtraction.difference(a, b)
        return self.Result

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a // b
