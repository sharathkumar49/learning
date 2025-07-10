"""
LeetCode 2091. Removing Minimum and Maximum From Array

Given an array nums, return the minimum number of operations to remove both the minimum and maximum element from the array.

Example:
Input: nums = [2,10,7,5,4,1,8,6]
Output: 5

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5
"""

def minimumDeletions(nums):
    n = len(nums)
    min_idx = nums.index(min(nums))
    max_idx = nums.index(max(nums))
    a, b = min(min_idx, max_idx), max(min_idx, max_idx)
    return min(b+1, n-a, a+1+n-b)

# Example usage:
# print(minimumDeletions([2,10,7,5,4,1,8,6]))  # Output: 5
