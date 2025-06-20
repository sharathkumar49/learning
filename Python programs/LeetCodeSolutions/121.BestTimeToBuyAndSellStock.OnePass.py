# 121. Best Time to Buy and Sell Stock (One Pass)
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
#
# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
#
# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
#
# Constraints:
# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^4

def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit

# Example usage
prices = [7,1,5,3,6,4]
print("Max profit (one pass):", maxProfit(prices))  # Output: 5
