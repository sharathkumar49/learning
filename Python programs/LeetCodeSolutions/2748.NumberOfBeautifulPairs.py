"""
LeetCode 2748. Number of Beautiful Pairs

Given nums, return the number of beautiful pairs.

Constraints:
- 2 <= nums.length <= 100
"""

def countBeautifulPairs(nums):
    def first(x):
        while x >= 10:
            x //= 10
        return x
    def last(x):
        return x % 10
    res = 0
    for a in nums:
        for b in nums:
            if a != b and gcd(first(a), last(b)) == 1:
                res += 1
    return res // 2
from math import gcd
# Example usage:
# print(countBeautifulPairs([2,5,1,4]))  # Output: 5
