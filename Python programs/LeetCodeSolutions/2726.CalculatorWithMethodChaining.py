"""
LeetCode 2726. Calculator With Method Chaining

Implement a calculator class with method chaining.

Constraints:
- 1 <= calls.length <= 10^5
"""
class Calculator:
    def __init__(self, value=0):
        self.value = value
    def add(self, n):
        self.value += n
        return self
    def subtract(self, n):
        self.value -= n
        return self
    def multiply(self, n):
        self.value *= n
        return self
    def divide(self, n):
        if n == 0:
            self.value = float('nan')
        else:
            self.value /= n
        return self
    def getResult(self):
        return self.value
# Example usage:
# calc = Calculator(10)
# print(calc.add(5).subtract(3).multiply(2).divide(4).getResult())  # Output: 6.0
