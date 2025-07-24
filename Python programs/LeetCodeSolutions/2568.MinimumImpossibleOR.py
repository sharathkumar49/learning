"""
LeetCode 2568. Minimum Impossible OR

Given an array, return the minimum impossible OR value.

Constraints:
- 1 <= nums.length <= 10^5
"""

def minImpossibleOR(nums):
    s = set(nums)
    x = 1
    while x in s:
        x <<= 1
    return x
# Example usage:
# print(minImpossibleOR([2,1]))  # Output: 4
