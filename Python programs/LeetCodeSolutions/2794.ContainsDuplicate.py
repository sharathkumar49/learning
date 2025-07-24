"""
LeetCode 2794. Contains Duplicate

Given nums, return True if any value appears at least twice.

Constraints:
- 1 <= nums.length <= 10^5
"""

def containsDuplicate(nums):
    return len(nums) != len(set(nums))
# Example usage:
# print(containsDuplicate([1,2,3,1]))  # Output: True
