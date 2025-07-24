"""
LeetCode 2764. Is Array Strictly Increasing

Given nums, return True if the array is strictly increasing.

Constraints:
- 1 <= nums.length <= 10^5
"""

def isStrictlyIncreasing(nums):
    return all(nums[i] < nums[i+1] for i in range(len(nums)-1))
# Example usage:
# print(isStrictlyIncreasing([1,2,3,4]))  # Output: True
