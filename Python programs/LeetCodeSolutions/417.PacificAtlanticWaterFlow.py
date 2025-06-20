"""
417. Pacific Atlantic Water Flow

Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, return a list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Constraints:
- m == heights.length
- n == heights[i].length
- 1 <= m, n <= 200
- 0 <= heights[i][j] <= 10^5
"""
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        m, n = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        def dfs(i, j, visited, prev):
            if (i, j) in visited or i < 0 or i >= m or j < 0 or j >= n or heights[i][j] < prev:
                return
            visited.add((i, j))
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                dfs(i+dx, j+dy, visited, heights[i][j])
        for i in range(m):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, n-1, atlantic, heights[i][n-1])
        for j in range(n):
            dfs(0, j, pacific, heights[0][j])
            dfs(m-1, j, atlantic, heights[m-1][j])
        return list(pacific & atlantic)

# Example usage:
heights = [
  [1,2,2,3,5],
  [3,2,3,4,4],
  [2,4,5,3,1],
  [6,7,1,4,5],
  [5,1,1,2,4]
]
print(Solution().pacificAtlantic(heights))
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
