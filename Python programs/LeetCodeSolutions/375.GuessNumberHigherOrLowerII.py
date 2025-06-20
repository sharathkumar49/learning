"""
375. Guess Number Higher or Lower II

We are playing the Guessing Game. Given n, find out how much money you need to guarantee a win.

Constraints:
- 1 <= n <= 200
"""
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for length in range(2, n + 1):
            for start in range(1, n - length + 2):
                end = start + length - 1
                dp[start][end] = min(max(dp[start][k-1], dp[k+1][end]) + k for k in range(start, end))
        return dp[1][n]

# Example usage:
n = 10
print(Solution().getMoneyAmount(n))  # Output: 16
