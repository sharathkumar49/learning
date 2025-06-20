"""
980. Unique Paths III
https://leetcode.com/problems/unique-paths-iii/

You are given an m x n integer array grid where grid[i][j] could be:
- 0: empty square
- 1: starting square
- 2: ending square
- -1: obstacle
Return the number of 4-directional walks from the starting square to the ending square, that visit every non-obstacle square exactly once.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 20
- 1 <= m * n <= 20

Example:
Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
"""
from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        empty = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    sx, sy = i, j
                elif grid[i][j] == 0:
                    empty += 1
        def dfs(x, y, remain):
            if not (0 <= x < m and 0 <= y < n and grid[x][y] >= 0):
                return 0
            if grid[x][y] == 2:
                return remain == 0
            tmp = grid[x][y]
            grid[x][y] = -2
            res = dfs(x+1, y, remain-1) + dfs(x-1, y, remain-1) + \
                  dfs(x, y+1, remain-1) + dfs(x, y-1, remain-1)
            grid[x][y] = tmp
            return res
        return dfs(sx, sy, empty)

# Example usage
if __name__ == "__main__":
    grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
    print(Solution().uniquePathsIII(grid))  # Output: 2
