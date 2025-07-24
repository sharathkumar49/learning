"""
LeetCode 2693. Call Function with Arguments

Implement a function to call another function with arguments.

Constraints:
- 1 <= calls.length <= 10^5
"""

def callFunction(fn, args):
    return fn(*args)
# Example usage:
# def add(a, b): return a + b
# print(callFunction(add, [2,3]))  # Output: 5
