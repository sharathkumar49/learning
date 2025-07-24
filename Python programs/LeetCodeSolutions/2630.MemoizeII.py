"""
LeetCode 2630. Memoize II

Implement a memoization decorator for a function with keyword arguments.

Constraints:
- 1 <= calls.length <= 10^5
"""

def memoize2(fn):
    cache = {}
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache:
            cache[key] = fn(*args, **kwargs)
        return cache[key]
    return wrapper
# Example usage:
# @memoize2
# def add(a, b=0): return a+b
# print(add(1, b=2))  # Output: 3
