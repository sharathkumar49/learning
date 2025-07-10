"""
LeetCode 2044. Count Number of Maximum Bitwise-OR Subsets

Given an integer array nums, return the number of subsets with the maximum bitwise OR.

Example:
Input: nums = [3,1]
Output: 2

Constraints:
- 1 <= nums.length <= 16
- 1 <= nums[i] <= 10^5
"""

def countMaxOrSubsets(nums):
    max_or = 0
    for x in nums:
        max_or |= x
    res = 0
    n = len(nums)
    for mask in range(1, 1 << n):
        curr = 0
        for i in range(n):
            if mask & (1 << i):
                curr |= nums[i]
        if curr == max_or:
            res += 1
    return res

# Example usage:
# print(countMaxOrSubsets([3,1]))  # Output: 2
