"""
517. Super Washing Machines

You have n washing machines in a line. Each washing machine has some dresses or is empty. Return the minimum number of moves to make all the dresses in the machines equal, or -1 if it is not possible.

Constraints:
- n == machines.length
- 1 <= n <= 10^4
- 0 <= machines[i] <= 10^5

Example:
Input: machines = [1,0,5]
Output: 3
"""

class Solution:
    def findMinMoves(self, machines: list) -> int:
        total = sum(machines)
        n = len(machines)
        if total % n != 0:
            return -1
        avg = total // n
        res = cnt = 0
        for m in machines:
            cnt += m - avg
            res = max(res, abs(cnt), m - avg)
        return res

# Example usage:
sol = Solution()
print(sol.findMinMoves([1,0,5]))  # Output: 3
