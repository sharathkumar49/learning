"""
542. 01 Matrix

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

Constraints:
- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 10^4
- 1 <= m * n <= 10^4
- mat[i][j] is either 0 or 1.

Example:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
"""

from collections import deque

class Solution:
    def updateMatrix(self, mat: list) -> list:
        m, n = len(mat), len(mat[0])
        res = [[float('inf')] * n for _ in range(m)]
        queue = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    res[i][j] = 0
                    queue.append((i, j))
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        while queue:
            x, y = queue.popleft()
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n and res[nx][ny] > res[x][y] + 1:
                    res[nx][ny] = res[x][y] + 1
                    queue.append((nx, ny))
        return res

# Example usage:
sol = Solution()
mat = [[0,0,0],[0,1,0],[1,1,1]]
print(sol.updateMatrix(mat))  # Output: [[0,0,0],[0,1,0],[1,2,1]]
