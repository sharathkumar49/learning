"""
LeetCode 2270. Number of Ways to Split Array

Given nums, return the number of ways to split the array into two parts with left sum >= right sum.

Example:
Input: nums = [10,4,-8,7]
Output: 2

Constraints:
- 2 <= nums.length <= 10^5
- -10^5 <= nums[i] <= 10^5
"""

def waysToSplitArray(nums):
    total = sum(nums)
    left = 0
    res = 0
    for i in range(len(nums)-1):
        left += nums[i]
        if left >= total - left:
            res += 1
    return res

# Example usage:
# print(waysToSplitArray([10,4,-8,7]))  # Output: 2
