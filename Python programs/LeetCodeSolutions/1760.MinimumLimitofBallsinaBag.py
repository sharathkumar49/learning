"""
LeetCode 1760. Minimum Limit of Balls in a Bag

Given an array nums and an integer maxOperations, return the minimum possible value of the maximum number of balls in a bag after performing at most maxOperations operations.

Example 1:
Input: nums = [9], maxOperations = 2
Output: 3

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= maxOperations <= 10^9
- 1 <= nums[i] <= 10^9
"""

def minimumSize(nums, maxOperations):
    l, r = 1, max(nums)
    while l < r:
        m = (l + r) // 2
        if sum((x-1)//m for x in nums) > maxOperations:
            l = m + 1
        else:
            r = m
    return l

# Example usage:
# nums = [9]
# maxOperations = 2
# print(minimumSize(nums, maxOperations))  # Output: 3
