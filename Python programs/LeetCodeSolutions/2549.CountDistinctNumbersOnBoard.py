"""
LeetCode 2549. Count Distinct Numbers on Board

Given n, return the count of distinct numbers on the board after operations.

Constraints:
- 1 <= n <= 100
"""

def distinctIntegers(n):
    return n-1 if n>1 else 1
# Example usage:
# print(distinctIntegers(5))  # Output: 4
