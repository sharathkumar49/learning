"""
LeetCode 1991. Find the Middle Index in Array

Given an array nums, return the leftmost middle index where the sum of the left equals the sum of the right.

Example:
Input: nums = [2,3,-1,8,4]
Output: 3

Constraints:
- 1 <= nums.length <= 100
- -1000 <= nums[i] <= 1000
"""

def findMiddleIndex(nums):
    total = sum(nums)
    left = 0
    for i, x in enumerate(nums):
        if left == total - left - x:
            return i
        left += x
    return -1

# Example usage:
# print(findMiddleIndex([2,3,-1,8,4]))  # Output: 3
