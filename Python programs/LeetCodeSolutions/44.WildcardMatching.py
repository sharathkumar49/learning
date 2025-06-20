# 44. Wildcard Matching
# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.
#
# Example 1:
# Input: s = "aa", p = "a"
# Output: false
#
# Example 2:
# Input: s = "aa", p = "*"
# Output: true
#
# Example 3:
# Input: s = "cb", p = "?a"
# Output: false
#
# Constraints:
# 0 <= s.length, p.length <= 2000
# s and p consist of only lowercase English letters.

def isMatch(s, p):
    m, n = len(s), len(p)
    dp = [[False] * (n+1) for _ in range(m+1)]
    dp[0][0] = True
    for j in range(1, n+1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-1]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if p[j-1] == '*':
                dp[i][j] = dp[i][j-1] or dp[i-1][j]
            elif p[j-1] == '?' or s[i-1] == p[j-1]:
                dp[i][j] = dp[i-1][j-1]
    return dp[m][n]

# Example usage
s = "aa"
p = "*"
print("Wildcard match:", isMatch(s, p))  # Output: True
