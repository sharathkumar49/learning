"""
LeetCode 1263. Minimum Moves to Move a Box to Their Target Location

A storekeeper is a game in which you have a 2D grid representing a warehouse, and you are tasked with moving a box to a target location with the minimum number of pushes. The grid contains walls, a box, a target, and a player. The player can move up, down, left, or right, and can push the box if the cell behind the box is empty. The goal is to find the minimum number of pushes required to move the box to the target location.

Constraints:
- 1 <= grid.length <= 20
- 1 <= grid[0].length <= 20
- grid contains only '.', '#', 'B', 'S', or 'T'
- There is exactly one box, one target, and one player in the grid.

Example:
Input: grid = [["#","#","#","#","#","#"],["#","T","#","#","#","#"],["#",".",".","B",".","#"],["#",".","#","#",".","#"],["#",".",".",".","S","#"],["#","#","#","#","#","#"]]
Output: 3

"""
from collections import deque

def minPushBox(grid):
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'S':
                sx, sy = i, j
            if grid[i][j] == 'B':
                bx, by = i, j
            if grid[i][j] == 'T':
                tx, ty = i, j
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    def inbounds(x, y):
        return 0 <= x < m and 0 <= y < n and grid[x][y] != '#'
    visited = set()
    queue = deque()
    queue.append((bx, by, sx, sy, 0))
    visited.add((bx, by, sx, sy))
    while queue:
        bx, by, px, py, pushes = queue.popleft()
        if (bx, by) == (tx, ty):
            return pushes
        for dx, dy in dirs:
            nbx, nby = bx + dx, by + dy
            opx, opy = bx - dx, by - dy
            if inbounds(nbx, nby) and inbounds(opx, opy):
                # Can player reach opx, opy without crossing box?
                seen = set()
                dq = deque([(px, py)])
                seen.add((px, py))
                while dq:
                    x, y = dq.popleft()
                    if (x, y) == (opx, opy):
                        break
                    for ddx, ddy in dirs:
                        nx, ny = x + ddx, y + ddy
                        if inbounds(nx, ny) and (nx, ny) not in seen and (nx, ny) != (bx, by):
                            seen.add((nx, ny))
                            dq.append((nx, ny))
                else:
                    continue
                if (nbx, nby, bx, by) not in visited:
                    visited.add((nbx, nby, bx, by))
                    queue.append((nbx, nby, bx, by, pushes + 1))
    return -1

# Example usage:
grid = [["#","#","#","#","#","#"],["#","T","#","#","#","#"],["#",".",".","B",".","#"],["#",".","#","#",".","#"],["#",".",".",".","S","#"],["#","#","#","#","#","#"]]
print(minPushBox(grid))  # Output: 3
