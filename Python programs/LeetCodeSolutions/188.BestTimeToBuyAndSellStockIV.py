"""
188. Best Time to Buy and Sell Stock IV
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

You are given an integer k and an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete at most k transactions.
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Constraints:
- 1 <= k <= 100
- 1 <= prices.length <= 1000
- 0 <= prices[i] <= 1000

Example 1:
Input: k = 2, prices = [2,4,1]
Output: 2

Example 2:
Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
"""
def maxProfit(k, prices):
    n = len(prices)
    if n == 0:
        return 0
    if k >= n // 2:
        return sum(max(prices[i+1] - prices[i], 0) for i in range(n-1))
    dp = [[0] * n for _ in range(k+1)]
    for t in range(1, k+1):
        max_diff = -prices[0]
        for d in range(1, n):
            dp[t][d] = max(dp[t][d-1], prices[d] + max_diff)
            max_diff = max(max_diff, dp[t-1][d] - prices[d])
    return dp[k][n-1]

# Example usage:
if __name__ == "__main__":
    print(maxProfit(2, [2,4,1]))           # Output: 2
    print(maxProfit(2, [3,2,6,5,0,3]))    # Output: 7
