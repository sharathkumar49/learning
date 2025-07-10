"""
LeetCode 1749. Maximum Absolute Sum of Any Subarray

Given an array nums, return the maximum absolute sum of any subarray.

Example 1:
Input: nums = [1,-3,2,3,-4]
Output: 5

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
"""

def maxAbsoluteSum(nums):
    max_sum = min_sum = res = 0
    for x in nums:
        max_sum = max(0, max_sum + x)
        min_sum = min(0, min_sum + x)
        res = max(res, abs(max_sum), abs(min_sum))
    return res

# Example usage:
# nums = [1,-3,2,3,-4]
# print(maxAbsoluteSum(nums))  # Output: 5
