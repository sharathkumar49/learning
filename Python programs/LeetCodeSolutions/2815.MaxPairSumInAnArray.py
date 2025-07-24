"""
LeetCode 2815. Max Pair Sum in an Array

Given nums, return the maximum pair sum.

Constraints:
- 2 <= nums.length <= 10^5
"""

def maxPairSum(nums):
    nums.sort()
    return nums[-1] + nums[-2]
# Example usage:
# print(maxPairSum([1,2,3,4]))  # Output: 7
