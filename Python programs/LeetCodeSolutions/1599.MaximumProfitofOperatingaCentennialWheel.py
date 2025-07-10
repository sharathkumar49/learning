"""
LeetCode 1599. Maximum Profit of Operating a Centennial Wheel

You are given an array customers where customers[i] is the number of customers arriving at the ith minute. Each ride can take up to 4 customers and costs boardingCost per customer. The running cost per minute is runningCost. Return the minimum number of minutes needed to achieve the maximum profit. If it is impossible, return -1.

Example 1:
Input: customers = [8,3], boardingCost = 5, runningCost = 6
Output: 3

Constraints:
- 1 <= customers.length <= 10^5
- 1 <= customers[i], boardingCost, runningCost <= 100
"""

def minOperationsMaxProfit(customers, boardingCost, runningCost):
    wait = profit = maxProfit = res = 0
    i = 0
    n = len(customers)
    ans = -1
    while wait > 0 or i < n:
        if i < n:
            wait += customers[i]
        board = min(4, wait)
        wait -= board
        profit += board * boardingCost - runningCost
        if profit > maxProfit:
            maxProfit = profit
            ans = i + 1
        i += 1
    return ans

# Example usage:
# customers = [8,3]
# boardingCost = 5
# runningCost = 6
# print(minOperationsMaxProfit(customers, boardingCost, runningCost))  # Output: 3
