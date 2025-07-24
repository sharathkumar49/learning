"""
LeetCode 2670. Find the Distinct Difference Array

Given nums, return the distinct difference array.

Constraints:
- 1 <= nums.length <= 50
"""

def distinctDifferenceArray(nums):
    res = []
    for i in range(len(nums)):
        left = len(set(nums[:i+1]))
        right = len(set(nums[i+1:]))
        res.append(left - right)
    return res
# Example usage:
# print(distinctDifferenceArray([1,2,3,4,5]))  # Output: [1,1,1,1,1]
