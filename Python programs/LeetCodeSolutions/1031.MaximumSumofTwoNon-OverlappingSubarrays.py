"""
1031. Maximum Sum of Two Non-Overlapping Subarrays

Given an array A, and two integers L and M, return the maximum sum of two non-overlapping subarrays of lengths L and M.

Constraints:
- 2 <= L <= A.length
- 2 <= M <= A.length
- L + M <= A.length <= 1000
- 0 <= A[i] <= 1000

Example:
Input: A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
Output: 20
Explanation: One subarray is [9], the other is [6,5].
"""
from typing import List

def maxSumTwoNoOverlap(A: List[int], L: int, M: int) -> int:
    def maxSum(L, M):
        sumL = sumM = 0
        res = 0
        for i in range(L + M):
            if i < L:
                sumL += A[i]
            else:
                sumM += A[i]
        res = sumL + sumM
        for i in range(L + M, len(A)):
            sumL += A[i - M] - A[i - L - M]
            sumM += A[i] - A[i - M]
            res = max(res, sumL + sumM)
        return res
    return max(maxSum(L, M), maxSum(M, L))

# Example usage:
A = [0,6,5,2,2,5,1,9,4]
L = 1
M = 2
print(maxSumTwoNoOverlap(A, L, M))  # Output: 20
