"""
LeetCode 1819. Number of Different Subsequences GCDs

Given an array nums, return the number of different greatest common divisors among all non-empty subsequences.

Example 1:
Input: nums = [6,10,3]
Output: 5

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 2 * 10^5
"""

def countDifferentSubsequenceGCDs(nums):
    nums_set = set(nums)
    max_num = max(nums)
    res = 0
    for x in range(1, max_num+1):
        g = 0
        for y in range(x, max_num+1, x):
            if y in nums_set:
                g = gcd(g, y) if g else y
            if g == x:
                break
        if g == x:
            res += 1
    return res

from math import gcd
# Example usage:
# nums = [6,10,3]
# print(countDifferentSubsequenceGCDs(nums))  # Output: 5
