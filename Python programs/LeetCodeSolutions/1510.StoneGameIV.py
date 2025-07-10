"""
LeetCode 1510. Stone Game IV

Alice and Bob take turns removing stones from a pile. The player who removes the last stone wins. Each turn, a player can remove any non-zero square number of stones. Given n, return true if Alice wins the game.

Constraints:
- 1 <= n <= 10^5

Example:
Input: n = 7
Output: False
"""
def winnerSquareGame(n):
    dp = [False] * (n+1)
    for i in range(1, n+1):
        j = 1
        while j*j <= i:
            if not dp[i - j*j]:
                dp[i] = True
                break
            j += 1
    return dp[n]

# Example usage:
n = 7
print(winnerSquareGame(n))  # Output: False
