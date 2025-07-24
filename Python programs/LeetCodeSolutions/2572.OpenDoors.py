"""
LeetCode 2572. Open Doors

Given n doors, return the number of doors that remain open after n passes.

Constraints:
- 1 <= n <= 10^5
"""

def openDoors(n):
    from math import isqrt
    return isqrt(n)
# Example usage:
# print(openDoors(10))  # Output: 3
