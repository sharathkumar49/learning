"""
LeetCode 1706. Where Will the Ball Fall

You have a grid of size m x n. Each cell has a diagonal board that redirects the ball to the left or right. Given a grid, return an array of the column indices where the ball falls out, or -1 if it gets stuck.

Example 1:
Input: grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
Output: [1,-1,-1,-1,-1]

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 100
- grid[i][j] is 1 or -1
"""

def findBall(grid):
    m, n = len(grid), len(grid[0])
    res = []
    for col in range(n):
        c = col
        for r in range(m):
            nc = c + grid[r][c]
            if nc < 0 or nc >= n or grid[r][c] != grid[r][nc]:
                c = -1
                break
            c = nc
        res.append(c)
    return res

# Example usage:
# grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
# print(findBall(grid))  # Output: [1,-1,-1,-1,-1]
