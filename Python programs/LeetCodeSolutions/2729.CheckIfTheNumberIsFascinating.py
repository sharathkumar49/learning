"""
LeetCode 2729. Check if The Number is Fascinating

Given n, return True if the number is fascinating.

Constraints:
- 100 <= n <= 999
"""

def isFascinating(n):
    s = str(n) + str(n*2) + str(n*3)
    return set(s) == set('123456789') and len(s) == 9
# Example usage:
# print(isFascinating(192))  # Output: True
