"""
LeetCode 2620. Counter

Implement a counter that increments by 1 each time it is called.

Constraints:
- 0 <= n <= 1000
"""

def createCounter(n):
    def counter():
        nonlocal n
        n += 1
        return n-1
    return counter
# Example usage:
# c = createCounter(10)
# print(c())  # Output: 10
# print(c())  # Output: 11
