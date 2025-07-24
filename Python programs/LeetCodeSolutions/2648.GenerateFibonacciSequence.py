"""
LeetCode 2648. Generate Fibonacci Sequence

Given n, return the first n Fibonacci numbers.

Constraints:
- 1 <= n <= 1000
"""

def generateFibonacci(n):
    if n == 0: return []
    if n == 1: return [0]
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib
# Example usage:
# print(generateFibonacci(5))  # Output: [0, 1, 1, 2, 3]
