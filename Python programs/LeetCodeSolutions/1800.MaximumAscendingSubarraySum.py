"""
LeetCode 1800. Maximum Ascending Subarray Sum

Given an array nums, return the maximum sum of any ascending subarray.

Example 1:
Input: nums = [10,20,30,5,10,50]
Output: 65

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100
"""

def maxAscendingSum(nums):
    res = curr = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            curr += nums[i]
        else:
            curr = nums[i]
        res = max(res, curr)
    return res

# Example usage:
# nums = [10,20,30,5,10,50]
# print(maxAscendingSum(nums))  # Output: 65
