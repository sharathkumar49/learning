"""
LeetCode 2425. Bitwise XOR of All Pairings

Given two arrays, return the bitwise XOR of all pairings.

Constraints:
- 1 <= nums1.length, nums2.length <= 10^5
"""

def xorAllNums(nums1, nums2):
    from functools import reduce
    if len(nums2)%2:
        x1 = reduce(lambda x,y: x^y, nums1, 0)
    else:
        x1 = 0
    if len(nums1)%2:
        x2 = reduce(lambda x,y: x^y, nums2, 0)
    else:
        x2 = 0
    return x1^x2

# Example usage:
# print(xorAllNums([2,1,3],[6,3]))  # Output: 2
