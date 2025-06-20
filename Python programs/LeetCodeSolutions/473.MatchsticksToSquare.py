"""
473. Matchsticks to Square

You are given an integer array matchsticks where matchsticks[i] is the length of the i-th matchstick. Return true if you can make a square with the matchsticks.

Constraints:
- 1 <= matchsticks.length <= 15
- 1 <= matchsticks[i] <= 10^8

Example:
Input: matchsticks = [1,1,2,2,2]
Output: true
"""

class Solution:
    def makesquare(self, matchsticks: list) -> bool:
        if not matchsticks or sum(matchsticks) % 4 != 0:
            return False
        side = sum(matchsticks) // 4
        matchsticks.sort(reverse=True)
        sides = [0] * 4
        def dfs(i):
            if i == len(matchsticks):
                return all(s == side for s in sides)
            for j in range(4):
                if sides[j] + matchsticks[i] <= side:
                    sides[j] += matchsticks[i]
                    if dfs(i+1):
                        return True
                    sides[j] -= matchsticks[i]
            return False
        return dfs(0)

# Example usage:
sol = Solution()
print(sol.makesquare([1,1,2,2,2]))  # Output: True
