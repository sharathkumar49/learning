"""
LeetCode 2326. Spiral Matrix IV

Given m, n, head, return the spiral matrix.

Example:
Input: m = 3, n = 3, head = [3,2,0,-4,-1,6]
Output: [[3,2,0],[6,-1,-4],[-1,-1,-1]]

Constraints:
- 1 <= m, n <= 100
"""

def spiralMatrix(m, n, head):
    mat = [[-1]*n for _ in range(m)]
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    x = y = d = 0
    for val in head:
        mat[x][y] = val
        nx, ny = x+dirs[d][0], y+dirs[d][1]
        if 0<=nx<m and 0<=ny<n and mat[nx][ny]==-1:
            x, y = nx, ny
        else:
            d = (d+1)%4
            x, y = x+dirs[d][0], y+dirs[d][1]
    return mat

# Example usage:
# print(spiralMatrix(3, 3, [3,2,0,-4,-1,6]))  # Output: [[3,2,0],[6,-1,-4],[-1,-1,-1]]
