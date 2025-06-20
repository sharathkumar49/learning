"""
1064. Fixed Point

Given an array A, return the smallest index i such that A[i] == i. If no such index exists, return -1.

Constraints:
- 1 <= A.length <= 10000
- -10^9 <= A[i] <= 10^9

Example:
Input: A = [-10,-5,0,3,7]
Output: 3
"""
from typing import List

def fixedPoint(A: List[int]) -> int:
    for i, num in enumerate(A):
        if i == num:
            return i
    return -1

# Example usage:
A = [-10,-5,0,3,7]
print(fixedPoint(A))  # Output: 3
