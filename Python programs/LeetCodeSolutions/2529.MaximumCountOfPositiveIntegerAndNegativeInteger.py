"""
LeetCode 2529. Maximum Count of Positive Integer and Negative Integer

Given an array, return the maximum count of positive and negative integers.

Constraints:
- 1 <= nums.length <= 10^5
"""

def maximumCount(nums):
    pos = sum(x > 0 for x in nums)
    neg = sum(x < 0 for x in nums)
    return max(pos, neg)
# Example usage:
# print(maximumCount([-2,-1,-1,1,2,3]))  # Output: 3
