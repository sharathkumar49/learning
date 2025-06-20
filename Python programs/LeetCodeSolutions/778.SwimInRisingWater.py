"""
778. Swim in Rising Water

You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point. On a rising water day, you can swim from the top-left to the bottom-right if the water level is at least the elevation of every cell you pass. Return the least time when you can swim to the bottom right.

Example 1:
Input: grid = [[0,2],[1,3]]
Output: 3

Example 2:
Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16

Constraints:
- n == grid.length
- n == grid[i].length
- 2 <= n <= 50
- 0 <= grid[i][j] < n^2
- Each value grid[i][j] is unique.
"""
import heapq

def swimInWater(grid):
    n = len(grid)
    visited = [[False]*n for _ in range(n)]
    heap = [(grid[0][0], 0, 0)]
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    while heap:
        time, x, y = heapq.heappop(heap)
        if x == n-1 and y == n-1:
            return time
        if visited[x][y]:
            continue
        visited[x][y] = True
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                heapq.heappush(heap, (max(time, grid[nx][ny]), nx, ny))
    return -1

# Example usage:
print(swimInWater([[0,2],[1,3]]))  # Output: 3
print(swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]))  # Output: 16
