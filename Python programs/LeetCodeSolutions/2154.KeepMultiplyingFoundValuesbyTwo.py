"""
LeetCode 2154. Keep Multiplying Found Values by Two

Given an integer array nums and an integer original, keep multiplying original by 2 if it exists in nums. Return the final value of original.

Example:
Input: nums = [5,3,6,1,12], original = 3
Output: 24

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i], original <= 1000
"""

def findFinalValue(nums, original):
    s = set(nums)
    while original in s:
        original *= 2
    return original

# Example usage:
# print(findFinalValue([5,3,6,1,12], 3))  # Output: 24
