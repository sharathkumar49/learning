# 10. Regular Expression Matching
# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*'.
#
# Example 1:
# Input: s = "aa", p = "a"
# Output: false
#
# Example 2:
# Input: s = "aa", p = "a*"
# Output: true
#
# Example 3:
# Input: s = "ab", p = ".*"
# Output: true
#
# Constraints:
# 1 <= s.length <= 20
# 1 <= p.length <= 30
# s contains only lowercase English letters.
# p contains only lowercase English letters, '.', and '*'.

def isMatch(s, p):
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = True
    for j in range(2, len(p) + 1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-2]
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j-1] == '.' or p[j-1] == s[i-1]:
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == '*':
                dp[i][j] = dp[i][j-2] or ((p[j-2] == s[i-1] or p[j-2] == '.') and dp[i-1][j])
    return dp[-1][-1]

# Example usage
s = "aa"
p = "a*"
print("Is match:", isMatch(s, p))  # Output: True
