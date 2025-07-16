"""
LeetCode 2229. Check if an Array Is Consecutive

Given an array nums, return true if it contains consecutive numbers.

Example:
Input: nums = [1,2,3,4]
Output: True

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 10^5
"""

def isConsecutive(nums):
    return len(nums) == max(nums) - min(nums) + 1 and len(set(nums)) == len(nums)

# Example usage:
# print(isConsecutive([1,2,3,4]))  # Output: True
