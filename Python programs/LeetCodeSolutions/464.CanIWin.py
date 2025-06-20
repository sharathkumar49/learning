"""
464. Can I Win

In the "100 game," two players take turns adding integers from 1 to maxChoosableInteger to a running total, and the player who first causes the running total to reach or exceed desiredTotal wins. Given maxChoosableInteger and desiredTotal, return true if the first player can force a win, otherwise false.

Constraints:
- 1 <= maxChoosableInteger <= 20
- 0 <= desiredTotal <= 300

Example:
Input: maxChoosableInteger = 10, desiredTotal = 11
Output: false
"""

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if (maxChoosableInteger + 1) * maxChoosableInteger // 2 < desiredTotal:
            return False
        memo = {}
        def dfs(used, total):
            if used in memo:
                return memo[used]
            for i in range(maxChoosableInteger):
                if not (used >> i) & 1:
                    if total + i + 1 >= desiredTotal or not dfs(used | (1 << i), total + i + 1):
                        memo[used] = True
                        return True
            memo[used] = False
            return False
        return dfs(0, 0)

# Example usage:
sol = Solution()
print(sol.canIWin(10, 11))  # Output: False
