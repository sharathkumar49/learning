"""
LeetCode 2632. Curry

Implement a curry function for a given function.

Constraints:
- 1 <= calls.length <= 10^5
"""

def curry(fn):
    def curried(*args):
        if len(args) >= fn.__code__.co_argcount:
            return fn(*args)
        return lambda *a: curried(*(args + a))
    return curried
# Example usage:
# def add(a, b): return a + b
# curried_add = curry(add)
# print(curried_add(1)(2))  # Output: 3
