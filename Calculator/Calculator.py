from MathOperations.addition import Addition

import math


class Calculator:

    public result;
    def __init__(self):
        pass

    def Sum(self, a, b):
        return Addition.sum(a, b);

    def Difference(self, a, b):
        return Subtraction.difference(a, b)

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a // b
