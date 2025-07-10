"""
LeetCode 1895. Largest Magic Square

Given an m x n integer grid, return the size (side length) of the largest magic square in grid.

Example:
Input: grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
Output: 3

Constraints:
- 2 <= m, n <= 50
- 1 <= grid[i][j] <= 10^6
"""

def largestMagicSquare(grid):
    m, n = len(grid), len(grid[0])
    row = [[0]*(n+1) for _ in range(m)]
    col = [[0]*(n) for _ in range(m+1)]
    for i in range(m):
        for j in range(n):
            row[i][j+1] = row[i][j] + grid[i][j]
            col[i+1][j] = col[i][j] + grid[i][j]
    for k in range(min(m, n), 1, -1):
        for i in range(m-k+1):
            for j in range(n-k+1):
                s = sum(grid[i+d][j+d] for d in range(k))
                if s != sum(grid[i+d][j+k-1-d] for d in range(k)):
                    continue
                if all(row[i+d][j+k]-row[i+d][j]==s for d in range(k)) and all(col[i+k][j+d]-col[i][j+d]==s for d in range(k)):
                    return k
    return 1

# Example usage:
# print(largestMagicSquare([[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]))  # Output: 3
