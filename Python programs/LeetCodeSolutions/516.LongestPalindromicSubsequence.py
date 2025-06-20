"""
516. Longest Palindromic Subsequence

Given a string s, return the length of the longest palindromic subsequence in s.

Constraints:
- 1 <= s.length <= 1000
- s consists only of lowercase English letters.

Example:
Input: s = "bbbab"
Output: 4
"""

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
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
sol = Solution()
print(sol.longestPalindromeSubseq("bbbab"))  # Output: 4
