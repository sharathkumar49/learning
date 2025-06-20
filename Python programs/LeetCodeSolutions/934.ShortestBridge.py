"""
934. Shortest Bridge
https://leetcode.com/problems/shortest-bridge/

You are given an n x n binary matrix grid where there are exactly two islands (groups of 1's connected 4-directionally). You may change 0's to 1's to connect the two islands. Return the smallest number of 0's you must flip to connect the two islands.

Constraints:
- n == grid.length == grid[i].length
- 2 <= n <= 100
- grid[i][j] is 0 or 1
- There are exactly two islands in grid.

Example:
Input: grid = [[0,1],[1,0]]
Output: 1
"""
from typing import List
from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def dfs(x, y, q):
            if x < 0 or x >= n or y < 0 or y >= n or grid[x][y] != 1:
                return
            grid[x][y] = 2
            q.append((x, y))
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                dfs(x+dx, y+dy, q)
        q = deque()
        found = False
        for i in range(n):
            if found:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j, q)
                    found = True
                    break
        steps = 0
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < n and 0 <= ny < n:
                        if grid[nx][ny] == 1:
                            return steps
                        if grid[nx][ny] == 0:
                            grid[nx][ny] = 2
                            q.append((nx, ny))
            steps += 1
        return -1

# Example usage
if __name__ == "__main__":
    grid = [[0,1],[1,0]]
    print(Solution().shortestBridge(grid))  # Output: 1
