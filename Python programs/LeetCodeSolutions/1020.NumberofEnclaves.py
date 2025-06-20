"""
1020. Number of Enclaves

Given a 2D array A, each cell is 0 (sea) or 1 (land). A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.
Return the number of land cells from which we cannot walk off the boundary of the grid.

Constraints:
- 1 <= A.length, A[0].length <= 500
- 0 <= A[i][j] <= 1

Example:
Input: A = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
"""
from typing import List

def numEnclaves(A: List[List[int]]) -> int:
    m, n = len(A), len(A[0])
    def dfs(i, j):
        if 0 <= i < m and 0 <= j < n and A[i][j] == 1:
            A[i][j] = 0
            for x, y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                dfs(x, y)
    for i in range(m):
        for j in range(n):
            if i in [0, m-1] or j in [0, n-1]:
                dfs(i, j)
    return sum(A[i][j] == 1 for i in range(m) for j in range(n))

# Example usage:
A = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
print(numEnclaves(A))  # Output: 3
