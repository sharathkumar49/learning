"""
499. The Maze III

Given a ball in a maze with empty spaces and walls, find the shortest distance for the ball to stop at the destination. The ball can only stop when it hits a wall. If there is no way for the ball to stop at the destination, return "impossible". If there are multiple shortest ways, return the lexicographically smallest way.

Constraints:
- 1 <= maze.length, maze[0].length <= 30
- maze[i][j] is 0 (empty) or 1 (wall)
- start.length == destination.length == 2

Example:
Input: maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], ball = [4,3], hole = [0,1]
Output: "impossible"
"""

import heapq

class Solution:
    def findShortestWay(self, maze: list, ball: list, hole: list) -> str:
        m, n = len(maze), len(maze[0])
        dirs = [(-1,0,'u'),(0,1,'r'),(1,0,'d'),(0,-1,'l')]
        heap = [(0, '', ball[0], ball[1])]
        visited = dict()
        while heap:
            dist, path, x, y = heapq.heappop(heap)
            if [x, y] == hole:
                return path
            if (x, y) in visited and visited[(x, y)] <= (dist, path):
                continue
            visited[(x, y)] = (dist, path)
            for dx, dy, dname in dirs:
                nx, ny, ndist = x, y, dist
                while 0 <= nx+dx < m and 0 <= ny+dy < n and maze[nx+dx][ny+dy] == 0:
                    nx += dx
                    ny += dy
                    ndist += 1
                    if [nx, ny] == hole:
                        break
                if (nx, ny) not in visited or visited[(nx, ny)] > (ndist, path + dname):
                    heapq.heappush(heap, (ndist, path + dname, nx, ny))
        return "impossible"

# Example usage:
sol = Solution()
maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]]
ball = [4,3]
hole = [0,1]
print(sol.findShortestWay(maze, ball, hole))  # Output: "impossible"
