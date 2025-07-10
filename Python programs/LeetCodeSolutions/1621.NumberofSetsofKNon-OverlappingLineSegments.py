"""
LeetCode 1621. Number of Sets of K Non-Overlapping Line Segments

Given n points on a line, return the number of ways to draw exactly k non-overlapping line segments such that each segment covers at least two points.

Example 1:
Input: n = 4, k = 2
Output: 1

Constraints:
- 2 <= n <= 1000
- 1 <= k <= n-1
"""

def numberOfSets(n, k):
    mod = 10**9+7
    dp = [[0]*(k+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
    for i in range(1, n+1):
        for j in range(1, k+1):
            dp[i][j] = (dp[i-1][j] + dp[i-1][j-1]*(i-1)) % mod
    return dp[n][k]

# Example usage:
# n = 4
# k = 2
# print(numberOfSets(n, k))  # Output: 1
