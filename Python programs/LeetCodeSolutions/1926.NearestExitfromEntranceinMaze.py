"""
LeetCode 1926. Nearest Exit from Entrance in Maze

Given a maze, return the minimum number of steps to the nearest exit from the entrance, or -1 if no exit exists.

Example:
Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
Output: 1

Constraints:
- maze.length == m
- maze[i].length == n
- 1 <= m, n <= 100
- entrance.length == 2
- 0 <= entrance[i] < maze.length
"""

from collections import deque

def nearestExit(maze, entrance):
    m, n = len(maze), len(maze[0])
    q = deque([(entrance[0], entrance[1], 0)])
    maze[entrance[0]][entrance[1]] = '+'
    while q:
        x, y, d = q.popleft()
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<m and 0<=ny<n and maze[nx][ny]=='.':
                if nx==0 or ny==0 or nx==m-1 or ny==n-1:
                    return d+1
                maze[nx][ny] = '+'
                q.append((nx, ny, d+1))
    return -1

# Example usage:
# print(nearestExit([["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], [1,2]))  # Output: 1
