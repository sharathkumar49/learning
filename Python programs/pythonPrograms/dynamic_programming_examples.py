# Dynamic programming: Fibonacci, coin change, LIS
def fib(n):
    dp = [0, 1]
    for i in range(2, n+1):
        dp.append(dp[-1] + dp[-2])
    return dp[n]

def coin_change(coins, amount):
    dp = [float('inf')] * (amount+1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount+1):
            dp[x] = min(dp[x], dp[x-coin]+1)
    return dp[amount] if dp[amount] != float('inf') else -1

def lis(nums):
    if not nums:
        return 0
    dp = [1]*len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

if __name__ == "__main__":
    print("Fibonacci(10):", fib(10))
    print("Coin change ([1,2,5], 11):", coin_change([1,2,5], 11))
    print("LIS [10,9,2,5,3,7,101,18]:", lis([10,9,2,5,3,7,101,18]))
