"""
LeetCode 2291. Maximum Profit from Trading Stocks

Given prices and fee, return the maximum profit you can achieve.

Example:
Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8

Constraints:
- 1 <= prices.length <= 10^5
- 1 <= prices[i], fee <= 10^5
"""

def maxProfit(prices, fee):
    cash, hold = 0, -prices[0]
    for price in prices[1:]:
        cash = max(cash, hold + price - fee)
        hold = max(hold, cash - price)
    return cash

# Example usage:
# print(maxProfit([1,3,2,8,4,9], 2))  # Output: 8
