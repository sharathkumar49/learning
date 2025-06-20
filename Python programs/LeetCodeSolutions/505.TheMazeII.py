"""
505. The Maze II

Given a ball in a maze with empty spaces and walls, find the shortest distance for the ball to stop at the destination. The ball can only stop when it hits a wall. If there is no way for the ball to stop at the destination, return -1.

Constraints:
- 1 <= maze.length, maze[0].length <= 100
- maze[i][j] is 0 (empty) or 1 (wall)
- start.length == destination.length == 2

Example:
Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]
Output: 12
"""

import heapq

class Solution:
    def shortestDistance(self, maze: list, start: list, destination: list) -> int:
        m, n = len(maze), len(maze[0])
        heap = [(0, start[0], start[1])]
        dist = [[float('inf')] * n for _ in range(m)]
        dist[start[0]][start[1]] = 0
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        while heap:
            d, x, y = heapq.heappop(heap)
            if [x, y] == destination:
                return d
            for dx, dy in dirs:
                nx, ny, nd = x, y, d
                while 0 <= nx+dx < m and 0 <= ny+dy < n and maze[nx+dx][ny+dy] == 0:
                    nx += dx
                    ny += dy
                    nd += 1
                if dist[nx][ny] > nd:
                    dist[nx][ny] = nd
                    heapq.heappush(heap, (nd, nx, ny))
        return -1

# Example usage:
sol = Solution()
maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start = [0,4]
destination = [4,4]
print(sol.shortestDistance(maze, start, destination))  # Output: 12
