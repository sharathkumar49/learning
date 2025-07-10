"""
LeetCode 2144. Minimum Cost of Buying Candies With Discount

Given the prices of candies, return the minimum cost of buying all the candies. For every two candies you buy, you get a third candy for free, as long as it is the cheapest one not yet bought.

Example:
Input: prices = [6,5,7,9,2,2]
Output: 23

Constraints:
- 1 <= prices.length <= 100
- 1 <= prices[i] <= 100
"""

def minimumCost(prices):
    prices.sort(reverse=True)
    total = 0
    for i, price in enumerate(prices):
        if (i+1) % 3 != 0:
            total += price
    return total

# Example usage:
# print(minimumCost([6,5,7,9,2,2]))  # Output: 23
