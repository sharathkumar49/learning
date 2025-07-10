"""
LeetCode 2110. Number of Smooth Descent Periods of a Stock

Given an array prices, return the total number of smooth descent periods of the stock.
A smooth descent period is a sequence where each element is exactly one less than the previous.

Example:
Input: prices = [3,2,1,4]
Output: 7

Constraints:
- 1 <= prices.length <= 10^5
- 1 <= prices[i] <= 10^5
"""

def getDescentPeriods(prices):
    res = 1
    curr = 1
    for i in range(1, len(prices)):
        if prices[i] == prices[i-1] - 1:
            curr += 1
        else:
            curr = 1
        res += curr
    return res

# Example usage:
# print(getDescentPeriods([3,2,1,4]))  # Output: 7
