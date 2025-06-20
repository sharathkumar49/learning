"""
1027. Longest Arithmetic Subsequence

Given an array A of integers, return the length of the longest arithmetic subsequence in A.

Constraints:
- 2 <= A.length <= 1000
- 0 <= A[i] <= 500

Example:
Input: A = [3,6,9,12]
Output: 4
Explanation: The whole array is an arithmetic sequence with difference 3.
"""
from typing import List

def longestArithSeqLength(A: List[int]) -> int:
    n = len(A)
    dp = [{} for _ in range(n)]
    res = 2
    for i in range(n):
        for j in range(i):
            diff = A[i] - A[j]
            dp[i][diff] = dp[j].get(diff, 1) + 1
            res = max(res, dp[i][diff])
    return res

# Example usage:
A = [3,6,9,12]
print(longestArithSeqLength(A))  # Output: 4
