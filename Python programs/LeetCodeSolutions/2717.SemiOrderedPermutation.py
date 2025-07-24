"""
LeetCode 2717. Semi-Ordered Permutation

Given nums, return the minimum number of adjacent swaps to make the permutation semi-ordered.

Constraints:
- 2 <= nums.length <= 10^5
"""

def semiOrderedPermutation(nums):
    n = len(nums)
    i = nums.index(1)
    j = nums.index(n)
    if i < j:
        return i + n - 1 - j
    else:
        return i + n - 2 - j
# Example usage:
# print(semiOrderedPermutation([2,1,4,3]))  # Output: 2
