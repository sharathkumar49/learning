"""
518. Coin Change 2

You are given an integer array coins representing coins of different denominations and an integer amount. Return the number of combinations that make up that amount.

Constraints:
- 1 <= coins.length <= 300
- 1 <= coins[i] <= 5000
- All the values of coins are unique.
- 0 <= amount <= 5000

Example:
Input: amount = 5, coins = [1,2,5]
Output: 4
"""

class Solution:
    def change(self, amount: int, coins: list) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[amount]

# Example usage:
sol = Solution()
print(sol.change(5, [1,2,5]))  # Output: 4
