"""
LeetCode 1746. Maximum Subarray Sum After One Operation

Given an array nums, you can choose one element and multiply it by -1. Return the maximum subarray sum possible after this operation.

Example 1:
Input: nums = [2,-1,-4,-3]
Output: 6

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
"""

def maximumSum(nums):
    n = len(nums)
    dp0 = nums[0]
    dp1 = -nums[0]
    res = max(dp0, dp1)
    for i in range(1, n):
        dp1 = max(dp0 - nums[i], dp1 + nums[i])
        dp0 = max(dp0 + nums[i], nums[i])
        res = max(res, dp0, dp1)
    return res

# Example usage:
# nums = [2,-1,-4,-3]
# print(maximumSum(nums))  # Output: 6
