"""
LeetCode 2759. Sum of Number of Pairs With Absolute Difference K

Given nums and k, return the sum of number of pairs with absolute difference k.

Constraints:
- 1 <= nums.length <= 10^5
"""

def countKDifference(nums, k):
    from collections import Counter
    c = Counter(nums)
    res = 0
    for x in c:
        res += c[x] * c.get(x+k, 0)
    return res
# Example usage:
# print(countKDifference([1,2,2,1], 1))  # Output: 4
