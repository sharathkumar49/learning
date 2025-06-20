"""
1035. Uncrossed Lines

Given two integer arrays A and B, return the maximum number of connecting lines (uncrossed lines) between A and B.

Constraints:
- 1 <= A.length, B.length <= 500
- 1 <= A[i], B[i] <= 2000

Example:
Input: A = [1,4,2], B = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
"""
from typing import List

def maxUncrossedLines(A: List[int], B: List[int]) -> int:
    m, n = len(A), len(B)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m):
        for j in range(n):
            if A[i] == B[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    return dp[m][n]

# Example usage:
A = [1,4,2]
B = [1,2,4]
print(maxUncrossedLines(A, B))  # Output: 2
