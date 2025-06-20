"""
LeetCode 712. Minimum ASCII Delete Sum for Two Strings

Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.

Example 1:
Input: s1 = "sea", s2 = "eat"
Output: 231

Example 2:
Input: s1 = "delete", s2 = "leet"
Output: 403

Constraints:
- 1 <= s1.length, s2.length <= 1000
- s1 and s2 consist of lowercase English letters.
"""
def minimumDeleteSum(s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m-1, -1, -1):
        dp[i][n] = dp[i+1][n] + ord(s1[i])
    for j in range(n-1, -1, -1):
        dp[m][j] = dp[m][j+1] + ord(s2[j])
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if s1[i] == s2[j]:
                dp[i][j] = dp[i+1][j+1]
            else:
                dp[i][j] = min(dp[i+1][j] + ord(s1[i]), dp[i][j+1] + ord(s2[j]))
    return dp[0][0]

# Example usage
if __name__ == "__main__":
    print(minimumDeleteSum("sea", "eat"))      # Output: 231
    print(minimumDeleteSum("delete", "leet"))  # Output: 403
