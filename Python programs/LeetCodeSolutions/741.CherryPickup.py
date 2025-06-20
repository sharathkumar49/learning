"""
LeetCode 741. Cherry Pickup

You are given an n x n grid representing a field of cherries, each cell is either empty (0), contains a cherry (1), or is a thorn (-1).
You have to collect the maximum number of cherries by traversing from (0,0) to (n-1,n-1) and back, moving only right or down on the way out and only left or up on the way back.

Example 1:
Input: grid = [[0,1,-1],[1,0,-1],[1,1,1]]
Output: 5

Constraints:
- n == grid.length
- n == grid[i].length
- 1 <= n <= 50
- grid[i][j] is -1, 0, or 1.
- grid[0][0] != -1 and grid[n-1][n-1] != -1
"""
from typing import List

def cherryPickup(grid: List[List[int]]) -> int:
    n = len(grid)
    dp = [[[-float('inf')]*n for _ in range(n)] for _ in range(n)]
    dp[0][0][0] = grid[0][0]
    for x1 in range(n):
        for y1 in range(n):
            for x2 in range(n):
                y2 = x1 + y1 - x2
                if y2 < 0 or y2 >= n or grid[x1][y1] == -1 or grid[x2][y2] == -1:
                    continue
                if x1 > 0:
                    dp[x1][y1][x2] = max(dp[x1][y1][x2], dp[x1-1][y1][x2])
                if y1 > 0:
                    dp[x1][y1][x2] = max(dp[x1][y1][x2], dp[x1][y1-1][x2])
                if x2 > 0:
                    dp[x1][y1][x2] = max(dp[x1][y1][x2], dp[x1][y1][x2-1])
                if y2 > 0:
                    dp[x1][y1][x2] = max(dp[x1][y1][x2], dp[x1][y1][x2])
                if dp[x1][y1][x2] < 0:
                    continue
                dp[x1][y1][x2] += grid[x2][y2] if (x1, y1) != (x2, y2) else 0
    return max(0, dp[n-1][n-1][n-1])

# Example usage
if __name__ == "__main__":
    print(cherryPickup([[0,1,-1],[1,0,-1],[1,1,1]]))  # Output: 5
