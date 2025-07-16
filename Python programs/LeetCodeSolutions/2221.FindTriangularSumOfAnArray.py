"""
LeetCode 2221. Find Triangular Sum of an Array

Given an array nums, return its triangular sum.

Example:
Input: nums = [1,2,3,4,5]
Output: 8

Constraints:
- 1 <= nums.length <= 1000
- 0 <= nums[i] <= 9
"""

def triangularSum(nums):
    while len(nums) > 1:
        nums = [(nums[i] + nums[i+1]) % 10 for i in range(len(nums)-1)]
    return nums[0]

# Example usage:
# print(triangularSum([1,2,3,4,5]))  # Output: 8
