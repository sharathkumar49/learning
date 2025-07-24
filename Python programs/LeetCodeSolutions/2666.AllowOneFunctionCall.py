"""
LeetCode 2666. Allow One Function Call

Implement a function wrapper that allows only one call.

Constraints:
- 1 <= calls.length <= 10^5
"""

def once(fn):
    called = False
    def wrapper(*args, **kwargs):
        nonlocal called
        if not called:
            called = True
            return fn(*args, **kwargs)
    return wrapper
# Example usage:
# def add(a, b): return a + b
# add_once = once(add)
# print(add_once(2,3))  # Output: 5
# print(add_once(2,3))  # Output: None
