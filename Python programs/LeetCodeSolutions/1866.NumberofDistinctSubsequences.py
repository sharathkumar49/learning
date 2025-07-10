"""
LeetCode 1866. Number of Distinct Subsequences

Given two strings s and t, return the number of distinct subsequences of s which equals t. The answer may be large, return it modulo 10^9 + 7.

Example:
Input: s = "rabbbit", t = "rabbit"
Output: 3

Constraints:
- 1 <= s.length, t.length <= 1000
- s and t consist of lowercase English letters.
"""

MOD = 10**9 + 7

def numDistinct(s, t):
    m, n = len(s), len(t)
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0] = 1
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % MOD
            else:
                dp[i][j] = dp[i-1][j]
    return dp[m][n]

# Example usage:
print(numDistinct("rabbbit", "rabbit"))  # Output: 3
