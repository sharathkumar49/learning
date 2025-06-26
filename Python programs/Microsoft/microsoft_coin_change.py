# Microsoft: Coin Change
# Given coins of different denominations and a total amount, compute the fewest number of coins needed to make up that amount.
# If not possible, return -1.

def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

if __name__ == "__main__":
    coins1 = [1,2,5]
    amount1 = 11
    print(coin_change(coins1, amount1))  # Output: 3
    coins2 = [2]
    amount2 = 3
    print(coin_change(coins2, amount2))  # Output: -1
