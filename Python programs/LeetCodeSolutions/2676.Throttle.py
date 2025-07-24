"""
LeetCode 2676. Throttle

Implement a throttle decorator for a function.

Constraints:
- 1 <= calls.length <= 10^5
"""
import threading, time
def throttle(fn, t):
    last = [0]
    def throttled(*args, **kwargs):
        now = time.time()
        if now - last[0] >= t/1000:
            last[0] = now
            return fn(*args, **kwargs)
    return throttled
# Example usage:
# def hello(): print("Hello!")
# throttled_hello = throttle(hello, 1000)
# throttled_hello()
