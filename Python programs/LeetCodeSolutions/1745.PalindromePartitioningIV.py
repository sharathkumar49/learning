"""
LeetCode 1745. Palindrome Partitioning IV

Given a string s, return true if it can be split into three palindromic substrings.

Example 1:
Input: s = "abcbdd"
Output: true

Constraints:
- 3 <= s.length <= 2000
- s consists only of lowercase English letters
"""

def checkPartitioning(s):
    n = len(s)
    dp = [[False]*n for _ in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j] and (j-i < 2 or dp[i+1][j-1]):
                dp[i][j] = True
    for i in range(1, n-1):
        for j in range(i, n-1):
            if dp[0][i-1] and dp[i][j] and dp[j+1][n-1]:
                return True
    return False

# Example usage:
# s = "abcbdd"
# print(checkPartitioning(s))  # Output: True
