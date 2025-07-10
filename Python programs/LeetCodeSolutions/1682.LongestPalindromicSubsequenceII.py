"""
LeetCode 1682. Longest Palindromic Subsequence II

Given a string s, return the length of the longest palindromic subsequence that is not a subsequence of another palindromic subsequence in s.

Example 1:
Input: s = "bbabab"
Output: 4

Constraints:
- 1 <= s.length <= 1000
- s consists of lowercase English letters.
"""

def longestPalindromeSubseq(s):
    n = len(s)
    dp = [[0]*n for _ in range(n)]
    for i in range(n-1, -1, -1):
        dp[i][i] = 1
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[0][n-1]

# Example usage:
# s = "bbabab"
# print(longestPalindromeSubseq(s))  # Output: 4
