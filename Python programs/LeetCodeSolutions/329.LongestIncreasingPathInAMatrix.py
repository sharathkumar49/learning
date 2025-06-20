"""
329. Longest Increasing Path in a Matrix

Given an m x n integers matrix, return the length of the longest increasing path in matrix.

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 200
- 0 <= matrix[i][j] <= 2^31 - 1
"""
from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        memo = [[0]*n for _ in range(m)]
        def dfs(i, j):
            if memo[i][j]:
                return memo[i][j]
            val = matrix[i][j]
            res = 1
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                x, y = i+dx, j+dy
                if 0<=x<m and 0<=y<n and matrix[x][y]>val:
                    res = max(res, 1+dfs(x, y))
            memo[i][j] = res
            return res
        return max(dfs(i, j) for i in range(m) for j in range(n))

# Example usage:
matrix = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
print(Solution().longestIncreasingPath(matrix))  # Output: 4
