"""
864. Shortest Path to Get All Keys

Given a grid, return the minimum number of steps to collect all keys. The grid contains walls, empty cells, and keys/locks.

Example 1:
Input: grid = ["@.a.#","###.#","b.A.B"]
Output: 8

Constraints:
- 1 <= grid.length <= 30
- 1 <= grid[0].length <= 30
- grid[i][j] is one of '.', '#', '@', 'a'-'f', 'A'-'F'.
"""
def shortestPathAllKeys(grid):
    from collections import deque
    m, n = len(grid), len(grid[0])
    keys = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '@':
                sx, sy = i, j
            elif grid[i][j].islower():
                keys |= 1 << (ord(grid[i][j]) - ord('a'))
    queue = deque([(sx, sy, 0, 0)])
    seen = set((sx, sy, 0))
    while queue:
        x, y, k, d = queue.popleft()
        if k == keys:
            return d
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<m and 0<=ny<n:
                cell = grid[nx][ny]
                nk = k
                if cell == '#':
                    continue
                if cell.islower():
                    nk |= 1 << (ord(cell) - ord('a'))
                if cell.isupper() and not (k & (1 << (ord(cell.lower()) - ord('a')))):
                    continue
                state = (nx, ny, nk)
                if state not in seen:
                    seen.add(state)
                    queue.append((nx, ny, nk, d+1))
    return -1

# Example usage:
print(shortestPathAllKeys(["@.a.#","###.#","b.A.B"]))  # Output: 8
