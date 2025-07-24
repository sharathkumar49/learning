"""
LeetCode 2733. Neither Minimum nor Maximum

Given nums, return any element that is neither the minimum nor the maximum.

Constraints:
- 2 <= nums.length <= 100
"""

def findNonMinOrMax(nums):
    nums = set(nums)
    if len(nums) < 3:
        return -1
    nums = sorted(nums)
    return nums[1]
# Example usage:
# print(findNonMinOrMax([3,2,1,4]))  # Output: 2
