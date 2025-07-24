"""
LeetCode 2623. Memoize

Implement a memoization decorator for a function.

Constraints:
- 1 <= calls.length <= 10^5
"""

def memoize(fn):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]
    return wrapper
# Example usage:
# @memoize
# def fib(n):
#     if n < 2: return n
#     return fib(n-1) + fib(n-2)
# print(fib(10))  # Output: 55
