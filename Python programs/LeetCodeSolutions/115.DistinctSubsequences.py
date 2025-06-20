"""
115. Distinct Subsequences
https://leetcode.com/problems/distinct-subsequences/

Given two strings s and t, return the number of distinct subsequences of s which equals t.

Constraints:
- 1 <= s.length, t.length <= 1000
- s and t consist of English letters.

Example:
Input: s = "rabbbit", t = "rabbit"
Output: 3
"""
def numDistinct(s: str, t: str) -> int:
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = 1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[m][n]

# Example usage:
if __name__ == "__main__":
    print(numDistinct("rabbbit", "rabbit"))  # Output: 3
    print(numDistinct("babgbag", "bag"))    # Output: 5
