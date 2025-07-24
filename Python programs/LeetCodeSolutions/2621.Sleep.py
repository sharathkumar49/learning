"""
LeetCode 2621. Sleep

Implement a sleep function that delays execution for a given time in milliseconds.

Constraints:
- 0 <= ms <= 10^4
"""
import time
def sleep(ms):
    time.sleep(ms/1000)
# Example usage:
# sleep(1000)  # Sleeps for 1 second
