"""
LeetCode 2806. Account Balance After Rounded Purchase

Given purchaseAmount, return the account balance after rounding.

Constraints:
- 1 <= purchaseAmount <= 100
"""

def accountBalanceAfterPurchase(purchaseAmount):
    return 100 - ((purchaseAmount + 4) // 10 * 10)
# Example usage:
# print(accountBalanceAfterPurchase(15))  # Output: 80
