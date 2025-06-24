"""
1131. Maximum of Absolute Value Expression

Given arrays arr1 and arr2, return the maximum value of |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j| for all 0 <= i, j < arr1.length.

Constraints:
- 2 <= arr1.length == arr2.length <= 40000
- -10^6 <= arr1[i], arr2[i] <= 10^6

Example:
Input: arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
Output: 13
"""
from typing import List

def maxAbsValExpr(arr1: List[int], arr2: List[int]) -> int:
    res = 0
    for p, q in [(1,1),(1,-1),(-1,1),(-1,-1)]:
        vals = [p*a + q*b + i for i, (a, b) in enumerate(zip(arr1, arr2))]
        res = max(res, max(vals) - min(vals))
    return res

# Example usage:
arr1 = [1,2,3,4]
arr2 = [-1,4,5,6]
print(maxAbsValExpr(arr1, arr2))  # Output: 13
