"""
1099. Two Sum Less Than K

Given an array A of integers and an integer K, return the maximum sum of two elements in A that is less than K. If no such pair exists, return -1.

Constraints:
- 2 <= A.length <= 100
- 1 <= A[i] <= 1000
- 1 <= K <= 2000

Example:
Input: A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
"""
from typing import List

def twoSumLessThanK(A: List[int], K: int) -> int:
    A.sort()
    left, right = 0, len(A) - 1
    res = -1
    while left < right:
        s = A[left] + A[right]
        if s < K:
            res = max(res, s)
            left += 1
        else:
            right -= 1
    return res

# Example usage:
A = [34,23,1,24,75,33,54,8]
K = 60
print(twoSumLessThanK(A, K))  # Output: 58
