"""
LeetCode 1835. Find XOR Sum of All Pairs Bitwise AND

Given two arrays arr1 and arr2, return the XOR sum of all pairs' bitwise AND.

Example 1:
Input: arr1 = [1,2,3], arr2 = [6,5]
Output: 0

Constraints:
- 1 <= arr1.length, arr2.length <= 10^5
- 0 <= arr1[i], arr2[i] <= 10^9
"""

def getXORSum(arr1, arr2):
    from functools import reduce
    from operator import ixor
    x1 = reduce(ixor, arr1, 0)
    x2 = reduce(ixor, arr2, 0)
    return x1 & x2

# Example usage:
# arr1 = [1,2,3]
# arr2 = [6,5]
# print(getXORSum(arr1, arr2))  # Output: 0
