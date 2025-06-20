"""
490. The Maze

Given a ball in a maze with empty spaces and walls, find if the ball can stop at the destination.

Constraints:
- 1 <= maze.length, maze[0].length <= 100
- maze[i][j] is 0 (empty) or 1 (wall)
- start.length == destination.length == 2

Example:
Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]
Output: true
"""

from collections import deque

class Solution:
    def hasPath(self, maze: list, start: list, destination: list) -> bool:
        m, n = len(maze), len(maze[0])
        visited = set()
        queue = deque([tuple(start)])
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        while queue:
            x, y = queue.popleft()
            if [x, y] == destination:
                return True
            for dx, dy in dirs:
                nx, ny = x, y
                while 0 <= nx+dx < m and 0 <= ny+dy < n and maze[nx+dx][ny+dy] == 0:
                    nx += dx
                    ny += dy
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
        return False

# Example usage:
sol = Solution()
maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start = [0,4]
destination = [4,4]
print(sol.hasPath(maze, start, destination))  # Output: True
