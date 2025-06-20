"""
123. Best Time to Buy and Sell Stock III
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

You are given an array prices where prices[i] is the price of a given stock on the i-th day.
Find the maximum profit you can achieve. You may complete at most two transactions.

Constraints:
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^5

Example:
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
"""
from typing import List

def maxProfit(prices: List[int]) -> int:
    if not prices:
        return 0
    n = len(prices)
    left_profits = [0] * n
    right_profits = [0] * n
    min_price = prices[0]
    for i in range(1, n):
        min_price = min(min_price, prices[i])
        left_profits[i] = max(left_profits[i-1], prices[i] - min_price)
    max_price = prices[-1]
    for i in range(n-2, -1, -1):
        max_price = max(max_price, prices[i])
        right_profits[i] = max(right_profits[i+1], max_price - prices[i])
    max_profit = 0
    for i in range(n):
        max_profit = max(max_profit, left_profits[i] + right_profits[i])
    return max_profit

# Example usage:
if __name__ == "__main__":
    print(maxProfit([3,3,5,0,0,3,1,4]))  # Output: 6
    print(maxProfit([1,2,3,4,5]))        # Output: 4
