"""
LeetCode 2784. Check if Array is Good

Given nums, return True if the array is good.

Constraints:
- 1 <= nums.length <= 10^5
"""

def isGood(nums):
    n = len(nums)
    return sorted(nums) == list(range(1, n)) + [n-1]
# Example usage:
# print(isGood([2,1,3,3]))  # Output: True
