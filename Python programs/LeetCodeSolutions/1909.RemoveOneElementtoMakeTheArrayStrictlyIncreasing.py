"""
LeetCode 1909. Remove One Element to Make the Array Strictly Increasing

Given an integer array nums, return true if it can become strictly increasing by removing at most one element.

Example:
Input: nums = [1,2,10,5,7]
Output: true

Constraints:
- 2 <= nums.length <= 1000
- 1 <= nums[i] <= 10^5
"""

def canBeIncreasing(nums):
    cnt = 0
    for i in range(1, len(nums)):
        if nums[i] <= nums[i-1]:
            cnt += 1
            if cnt > 1:
                return False
            if i > 1 and nums[i] <= nums[i-2]:
                nums[i] = nums[i-1]
    return True

# Example usage:
# print(canBeIncreasing([1,2,10,5,7]))  # Output: True
