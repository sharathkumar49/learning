"""
LeetCode 2241. Design an ATM

Design an ATM with deposit and withdraw operations.

Example:
Input: ["ATM","deposit","withdraw"], [[],[[0,0,1,2,1],[600]]]
Output: [null,null,[0,0,1,0,1]]

Constraints:
- 1 <= transactions.length <= 10^5
"""

class ATM:
    def __init__(self):
        self.notes = [0]*5
        self.values = [20,50,100,200,500]
    def deposit(self, banknotesCount):
        for i in range(5):
            self.notes[i] += banknotesCount[i]
    def withdraw(self, amount):
        res = [0]*5
        for i in range(4,-1,-1):
            take = min(self.notes[i], amount//self.values[i])
            res[i] = take
            amount -= take*self.values[i]
        if amount == 0:
            for i in range(5):
                self.notes[i] -= res[i]
            return res
        return [-1]

# Example usage:
# atm = ATM()
# atm.deposit([0,0,1,2,1])
# print(atm.withdraw(600))  # Output: [0,0,1,0,1]
