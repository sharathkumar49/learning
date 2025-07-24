"""
LeetCode 2596. Check Knight Tour Configuration

Given a grid, check if it is a valid knight tour configuration.

Constraints:
- 1 <= n <= 6
"""

def checkValidGrid(grid):
    n = len(grid)
    pos = [None]*(n*n)
    for i in range(n):
        for j in range(n):
            pos[grid[i][j]] = (i, j)
    for k in range(1, n*n):
        x0, y0 = pos[k-1]
        x1, y1 = pos[k]
        if (abs(x0-x1), abs(y0-y1)) not in [(1,2),(2,1)]:
            return False
    return pos[0] == (0,0)
# Example usage:
# print(checkValidGrid([[0,11,16,5,20],[17,4,1,12,7],[10,15,8,21,6],[3,18,23,14,13],[24,9,2,19,22]]))  # Output: True
