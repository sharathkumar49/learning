"""
LeetCode 1312. Minimum Insertion Steps to Make a String Palindrome

Given a string s, return the minimum number of insertions needed to make s a palindrome.

Constraints:
- 1 <= s.length <= 500
- s consists of lowercase English letters only.

Example:
Input: s = "zzazz"
Output: 0
"""
def minInsertions(s):
    n = len(s)
    dp = [[0]*n for _ in range(n)]
    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i+l-1
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
    return dp[0][n-1]

# Example usage:
s = "zzazz"
print(minInsertions(s))  # Output: 0
