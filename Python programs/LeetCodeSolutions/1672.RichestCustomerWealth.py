"""
LeetCode 1672. Richest Customer Wealth

Given a 2D array accounts, return the maximum wealth of any customer.

Example 1:
Input: accounts = [[1,2,3],[3,2,1]]
Output: 6

Constraints:
- 1 <= accounts.length, accounts[i].length <= 50
- 1 <= accounts[i][j] <= 100
"""

def maximumWealth(accounts):
    return max(map(sum, accounts))

# Example usage:
# accounts = [[1,2,3],[3,2,1]]
# print(maximumWealth(accounts))  # Output: 6
