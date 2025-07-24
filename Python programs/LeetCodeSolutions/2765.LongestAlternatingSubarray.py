"""
LeetCode 2765. Longest Alternating Subarray

Given nums, return the length of the longest alternating subarray.

Constraints:
- 1 <= nums.length <= 10^5
"""

def alternatingSubarray(nums):
    res = cur = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            cur += 1
        else:
            cur = 1
        res = max(res, cur)
    return res
# Example usage:
# print(alternatingSubarray([1,2,1,2,1]))  # Output: 5
