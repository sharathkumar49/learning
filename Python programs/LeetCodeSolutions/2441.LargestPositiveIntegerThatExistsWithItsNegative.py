"""
LeetCode 2441. Largest Positive Integer That Exists With Its Negative

Given an array, return the largest positive integer that exists with its negative.

Constraints:
- 1 <= nums.length <= 2000
"""

def findMaxK(nums):
    s = set(nums)
    return max([x for x in s if -x in s and x > 0], default=-1)

# Example usage:
# print(findMaxK([-1,2,-3,3]))  # Output: 3
