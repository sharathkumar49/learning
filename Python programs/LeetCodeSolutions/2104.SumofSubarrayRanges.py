"""
LeetCode 2104. Sum of Subarray Ranges

Given an integer array nums, return the sum of ranges of all subarrays.

Example:
Input: nums = [1,2,3]
Output: 4

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
"""

def subArrayRanges(nums):
    n = len(nums)
    res = 0
    for i in range(n):
        min_val = max_val = nums[i]
        for j in range(i+1, n):
            min_val = min(min_val, nums[j])
            max_val = max(max_val, nums[j])
            res += max_val - min_val
    return res

# Example usage:
# print(subArrayRanges([1,2,3]))  # Output: 4
