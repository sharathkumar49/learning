"""
1162. As Far from Land as Possible

Given an n x n grid containing only 0s (water) and 1s (land), return the maximum distance from a water cell to the nearest land cell. If no land or water exists, return -1.

Constraints:
- 1 <= n <= 100
- grid[i][j] is 0 or 1

Example:
Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
Output: 2

"""
def maxDistance(grid):
    from collections import deque
    n = len(grid)
    q = deque()
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                q.append((i, j))
    if not q or len(q) == n * n:
        return -1
    dist = -1
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = x+dx, y+dy
                if 0<=nx<n and 0<=ny<n and grid[nx][ny]==0:
                    grid[nx][ny] = 2
                    q.append((nx, ny))
        dist += 1
    return dist

# Example usage
if __name__ == "__main__":
    print(maxDistance([[1,0,1],[0,0,0],[1,0,1]]))  # Output: 2
