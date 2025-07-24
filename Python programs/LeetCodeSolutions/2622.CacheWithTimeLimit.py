"""
LeetCode 2622. Cache With Time Limit

Implement a cache with a time limit for each key.

Constraints:
- 1 <= calls.length <= 10^5
"""
import time
class TimeLimitedCache:
    def __init__(self):
        self.cache = {}
    def set(self, key, value, duration):
        self.cache[key] = (value, time.time() + duration/1000)
        return True
    def get(self, key):
        v = self.cache.get(key)
        if v and v[1] > time.time():
            return v[0]
        return -1
    def count(self):
        now = time.time()
        return sum(1 for v in self.cache.values() if v[1] > now)
# Example usage:
# cache = TimeLimitedCache()
# cache.set(1, 42, 1000)
# print(cache.get(1))  # Output: 42
# time.sleep(1)
# print(cache.get(1))  # Output: -1
