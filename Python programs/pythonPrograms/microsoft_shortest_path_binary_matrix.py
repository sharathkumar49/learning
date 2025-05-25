# Microsoft: Find the Shortest Path in Binary Matrix
# Given an n x n binary matrix, return the length of the shortest clear path from top-left to bottom-right, or -1 if no such path.
from collections import deque

def shortest_path_binary_matrix(grid):
    n = len(grid)
    if grid[0][0] or grid[n-1][n-1]:
        return -1
    queue = deque([(0,0,1)])
    visited = set((0,0))
    directions = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
    while queue:
        x, y, d = queue.popleft()
        if x == n-1 and y == n-1:
            return d
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<n and not grid[nx][ny] and (nx,ny) not in visited:
                visited.add((nx,ny))
                queue.append((nx,ny,d+1))
    return -1

if __name__ == "__main__":
    grid1 = [
        [0,1],
        [1,0]
    ]
    print(shortest_path_binary_matrix([row[:] for row in grid1]))  # Output: 2
    grid2 = [
        [0,0,0],
        [1,1,0],
        [1,1,0]
    ]
    print(shortest_path_binary_matrix([row[:] for row in grid2]))  # Output: 4
