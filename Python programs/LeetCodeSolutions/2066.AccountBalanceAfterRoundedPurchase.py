"""
LeetCode 2066. Account Balance After Rounded Purchase

Given an integer purchaseAmount, return the account balance after rounding up to the nearest multiple of 10 and subtracting from 100.

Example:
Input: purchaseAmount = 15
Output: 80

Constraints:
- 1 <= purchaseAmount <= 100
"""

def accountBalanceAfterPurchase(purchaseAmount):
    return 100 - ((purchaseAmount + 9) // 10) * 10

# Example usage:
# print(accountBalanceAfterPurchase(15))  # Output: 80
