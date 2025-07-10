"""
LeetCode 1913. Maximum Product Difference Between Two Pairs

Given an integer array nums, return the maximum product difference between two pairs.

Example:
Input: nums = [5,6,2,7,4]
Output: 34

Constraints:
- 4 <= nums.length <= 10^4
- 1 <= nums[i] <= 10^4
"""

def maxProductDifference(nums):
    nums.sort()
    return nums[-1]*nums[-2] - nums[0]*nums[1]

# Example usage:
# print(maxProductDifference([5,6,2,7,4]))  # Output: 34
