"""
LeetCode 2344. Minimum Deletions to Make Array Divisible

Given nums and numsDivide, return the minimum deletions to make nums divisible by numsDivide.

Example:
Input: nums = [3,7,9], numsDivide = [2,4]
Output: -1

Constraints:
- 1 <= nums.length, numsDivide.length <= 10^5
"""

def minDeletions(nums, numsDivide):
    from math import gcd
    from functools import reduce
    g = reduce(gcd, numsDivide)
    nums.sort()
    for i, num in enumerate(nums):
        if g % num == 0:
            return i
    return -1

# Example usage:
# print(minDeletions([3,7,9], [2,4]))  # Output: -1
