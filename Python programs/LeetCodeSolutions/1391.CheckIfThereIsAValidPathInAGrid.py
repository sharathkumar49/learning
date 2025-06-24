"""
LeetCode 1391. Check if There is a Valid Path in a Grid

Given a m x n grid. Each cell of grid has a type (1 to 6) that determines the directions you can move from that cell. Return true if there is a valid path from the top-left cell to the bottom-right cell.

Constraints:
- 1 <= m, n <= 300
- grid[i][j] in [1,6]

Example:
Input: grid = [[2,4,3],[6,5,2]]
Output: true
"""
def hasValidPath(grid):
    m, n = len(grid), len(grid[0])
    from collections import deque
    dirs = {1:[(0,-1),(0,1)],2:[(-1,0),(1,0)],3:[(0,-1),(1,0)],4:[(0,1),(1,0)],5:[(0,-1),(-1,0)],6:[(0,1),(-1,0)]}
    def connect(a, b, da, db):
        return (da == -a and db == -b)
    q = deque([(0,0)])
    seen = set([(0,0)])
    while q:
        x, y = q.popleft()
        if (x, y) == (m-1, n-1):
            return True
        for dx, dy in dirs[grid[x][y]]:
            nx, ny = x+dx, y+dy
            if 0<=nx<m and 0<=ny<n and (nx,ny) not in seen:
                for ddx, ddy in dirs[grid[nx][ny]]:
                    if connect(dx, dy, ddx, ddy):
                        seen.add((nx,ny))
                        q.append((nx,ny))
    return False

# Example usage:
grid = [[2,4,3],[6,5,2]]
print(hasValidPath(grid))  # Output: True
