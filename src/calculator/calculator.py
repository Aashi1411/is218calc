from src.calculator.addition import addition
from src.calculator.subtraction import subtraction


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def sub(self, a, b):
        self.result = subtraction(a, b)
        return self.result