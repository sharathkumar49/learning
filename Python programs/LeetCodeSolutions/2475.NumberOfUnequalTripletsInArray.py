"""
LeetCode 2475. Number of Unequal Triplets in Array

Given an array, return the number of unequal triplets.

Constraints:
- 3 <= nums.length <= 100
"""

def unequalTriplets(nums):
    from collections import Counter
    cnt = Counter(nums)
    n = len(nums)
    res = 0
    left = 0
    for v in cnt.values():
        res += left * v * (n-left-v)
        left += v
    return res

# Example usage:
# print(unequalTriplets([4,4,2,4,3]))  # Output: 3
