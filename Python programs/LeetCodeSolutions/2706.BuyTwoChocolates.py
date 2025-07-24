"""
LeetCode 2706. Buy Two Chocolates

Given prices and money, return the money left after buying two cheapest chocolates, or money if not enough.

Constraints:
- 2 <= prices.length <= 100
"""

def buyChoco(prices, money):
    prices.sort()
    return money - prices[0] - prices[1] if prices[0] + prices[1] <= money else money
# Example usage:
# print(buyChoco([1,2,2], 3))  # Output: 0
