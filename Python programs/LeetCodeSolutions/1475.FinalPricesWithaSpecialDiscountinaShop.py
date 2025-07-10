"""
LeetCode 1475. Final Prices With a Special Discount in a Shop

Given the array prices where prices[i] is the price of the ith item in a shop, return an array where the value at index i is the final price you will pay for the ith item, considering a special discount.

Constraints:
- 1 <= prices.length <= 500
- 1 <= prices[i] <= 10^3

Example:
Input: prices = [8,4,6,2,3]
Output: [4,2,4,2,3]
"""
def finalPrices(prices):
    n = len(prices)
    res = prices[:]
    for i in range(n):
        for j in range(i+1, n):
            if prices[j] <= prices[i]:
                res[i] -= prices[j]
                break
    return res

# Example usage:
prices = [8,4,6,2,3]
print(finalPrices(prices))  # Output: [4,2,4,2,3]
