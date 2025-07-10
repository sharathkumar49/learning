"""
LeetCode 2043. Simple Bank System

Design a bank system that supports deposit, withdraw, and transfer operations.

Example:
Input: ["Bank","deposit","withdraw","transfer"], [[[10,100,20]],[0,10],[1,20],[0,1,30]]
Output: [null,null,null,null]

Constraints:
- 1 <= balance.length <= 10^5
- 1 <= amount <= 10^12
"""

class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.n = len(balance)
    def _valid(self, account):
        return 0 <= account < self.n
    def transfer(self, account1, account2, money):
        if not self._valid(account1) or not self._valid(account2) or self.balance[account1] < money:
            return False
        self.balance[account1] -= money
        self.balance[account2] += money
        return True
    def deposit(self, account, money):
        if not self._valid(account):
            return False
        self.balance[account] += money
        return True
    def withdraw(self, account, money):
        if not self._valid(account) or self.balance[account] < money:
            return False
        self.balance[account] -= money
        return True

# Example usage:
# bank = Bank([10,100,20])
# print(bank.deposit(0, 10))  # Output: True
# print(bank.withdraw(1, 20)) # Output: True
# print(bank.transfer(0, 1, 30)) # Output: True
