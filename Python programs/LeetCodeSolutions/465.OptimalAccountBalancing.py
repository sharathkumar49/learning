"""
465. Optimal Account Balancing

A group of friends went on a vacation and sometimes lent each other money. Given a list of transactions, return the minimum number of transactions required to settle the debt.

Constraints:
- 1 <= transactions.length <= 8
- transactions[i].length == 3
- 0 <= transactions[i][0], transactions[i][1] < 12
- 1 <= transactions[i][2] <= 100

Example:
Input: transactions = [[0,1,10],[2,0,5]]
Output: 2
"""

class Solution:
    def minTransfers(self, transactions: list) -> int:
        from collections import defaultdict
        balance = defaultdict(int)
        for f, t, amt in transactions:
            balance[f] -= amt
            balance[t] += amt
        debts = [v for v in balance.values() if v]
        def dfs(start):
            while start < len(debts) and debts[start] == 0:
                start += 1
            if start == len(debts):
                return 0
            res = float('inf')
            for i in range(start+1, len(debts)):
                if debts[i] * debts[start] < 0:
                    debts[i] += debts[start]
                    res = min(res, 1 + dfs(start+1))
                    debts[i] -= debts[start]
            return res if res != float('inf') else 0
        return dfs(0)

# Example usage:
sol = Solution()
print(sol.minTransfers([[0,1,10],[2,0,5]]))  # Output: 2
