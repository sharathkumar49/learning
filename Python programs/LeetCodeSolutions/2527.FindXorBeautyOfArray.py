"""
LeetCode 2527. Find Xor-Beauty of Array

Given an array, return the xor-beauty of the array.

Constraints:
- 1 <= nums.length <= 10^5
"""

def xorBeauty(nums):
    from functools import reduce
    return reduce(lambda x,y: x^y, nums)
# Example usage:
# print(xorBeauty([1,2,3]))  # Output: 0
