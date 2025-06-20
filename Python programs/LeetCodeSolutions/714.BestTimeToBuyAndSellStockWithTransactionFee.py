"""
LeetCode 714. Best Time to Buy and Sell Stock with Transaction Fee

You are given an array prices where prices[i] is the price of a given stock on the i-th day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

Example 1:
Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8

Example 2:
Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6

Constraints:
- 1 <= prices.length <= 5 * 10^4
- 1 <= prices[i] < 5 * 10^4
- 0 <= fee < 5 * 10^4
"""
from typing import List

def maxProfit(prices: List[int], fee: int) -> int:
    cash, hold = 0, -prices[0]
    for price in prices[1:]:
        cash = max(cash, hold + price - fee)
        hold = max(hold, cash - price)
    return cash

# Example usage
if __name__ == "__main__":
    print(maxProfit([1,3,2,8,4,9], 2))  # Output: 8
    print(maxProfit([1,3,7,5,10,3], 3)) # Output: 6
