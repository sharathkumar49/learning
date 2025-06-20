"""
174. Dungeon Game
https://leetcode.com/problems/dungeon-game/

The knight's health has to be at least 1 at all times. Given a 2D grid dungeon, return the knight's minimum initial health so that he can rescue the princess.

Constraints:
- m == dungeon.length
- n == dungeon[i].length
- 1 <= m, n <= 200
- -1000 <= dungeon[i][j] <= 1000

Example:
Input: dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
Output: 7
"""
from typing import List

def calculateMinimumHP(dungeon: List[List[int]]) -> int:
    m, n = len(dungeon), len(dungeon[0])
    dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
    dp[m][n-1] = dp[m-1][n] = 1
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            need = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
            dp[i][j] = max(1, need)
    return dp[0][0]

# Example usage:
if __name__ == "__main__":
    dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
    print(calculateMinimumHP(dungeon))  # Output: 7
