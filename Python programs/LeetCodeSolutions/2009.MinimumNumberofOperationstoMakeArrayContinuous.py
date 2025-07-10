"""
LeetCode 2009. Minimum Number of Operations to Make Array Continuous

Given an integer array nums, return the minimum number of operations to make nums continuous.

Example:
Input: nums = [4,2,5,3]
Output: 0

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
"""

def minOperations(nums):
    nums = sorted(set(nums))
    n = len(nums)
    res = float('inf')
    for i, x in enumerate(nums):
        y = x + len(nums) - 1
        j = bisect.bisect_right(nums, y)
        res = min(res, n - (j - i))
    return res

import bisect
# Example usage:
# print(minOperations([4,2,5,3]))  # Output: 0
