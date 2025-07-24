"""
LeetCode 2627. Debounce

Implement a debounce decorator for a function.

Constraints:
- 1 <= calls.length <= 10^5
"""
import threading
def debounce(fn, wait):
    timer = None
    def debounced(*args, **kwargs):
        nonlocal timer
        if timer:
            timer.cancel()
        timer = threading.Timer(wait/1000, lambda: fn(*args, **kwargs))
        timer.start()
    return debounced
# Example usage:
# def hello(): print("Hello!")
# debounced_hello = debounce(hello, 1000)
# debounced_hello()
