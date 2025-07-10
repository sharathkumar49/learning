"""
LeetCode 1827. Minimum Operations to Make the Array Increasing

Given an array nums, return the minimum number of operations to make it strictly increasing.

Example 1:
Input: nums = [1,1,1]
Output: 3

Constraints:
- 1 <= nums.length <= 5000
- 1 <= nums[i] <= 10^4
"""

def minOperations(nums):
    res = 0
    for i in range(1, len(nums)):
        if nums[i] <= nums[i-1]:
            res += nums[i-1] - nums[i] + 1
            nums[i] = nums[i-1] + 1
    return res

# Example usage:
# nums = [1,1,1]
# print(minOperations(nums))  # Output: 3
