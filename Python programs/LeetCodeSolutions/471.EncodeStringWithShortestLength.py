"""
471. Encode String with Shortest Length

Given a non-empty string s, encode the string such that its encoded length is the shortest. The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is repeated exactly k times.

Constraints:
- 1 <= s.length <= 150
- s consists of lowercase English letters only.

Example:
Input: s = "aaa"
Output: "aaa"
"""

class Solution:
    def encode(self, s: str) -> str:
        n = len(s)
        dp = [['' for _ in range(n)] for _ in range(n)]
        for l in range(1, n+1):
            for i in range(n-l+1):
                j = i + l - 1
                substr = s[i:j+1]
                dp[i][j] = substr
                for k in range(i, j):
                    if len(dp[i][k] + dp[k+1][j]) < len(dp[i][j]):
                        dp[i][j] = dp[i][k] + dp[k+1][j]
                for k in range(1, l//2+1):
                    if l % k == 0 and substr == substr[:k] * (l//k):
                        encoded = f"{l//k}[{dp[i][i+k-1]}]"
                        if len(encoded) < len(dp[i][j]):
                            dp[i][j] = encoded
        return dp[0][n-1]

# Example usage:
sol = Solution()
print(sol.encode("aaa"))  # Output: "aaa"
