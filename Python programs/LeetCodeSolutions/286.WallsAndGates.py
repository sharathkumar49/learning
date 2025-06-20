"""
286. Walls and Gates
https://leetcode.com/problems/walls-and-gates/

You are given an m x n grid rooms initialized with these three possible values:
- -1: A wall or an obstacle.
- 0: A gate.
- INF: Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Constraints:
- m == rooms.length
- n == rooms[i].length
- 1 <= m, n <= 250
- rooms[i][j] is -1, 0, or 2147483647.

Example 1:
Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
"""
def wallsAndGates(rooms):
    from collections import deque
    if not rooms:
        return
    m, n = len(rooms), len(rooms[0])
    queue = deque()
    for i in range(m):
        for j in range(n):
            if rooms[i][j] == 0:
                queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and rooms[nx][ny] == 2147483647:
                rooms[nx][ny] = rooms[x][y] + 1
                queue.append((nx, ny))

# Example usage:
if __name__ == "__main__":
    INF = 2147483647
    rooms = [
        [INF,-1,0,INF],
        [INF,INF,INF,-1],
        [INF,-1,INF,-1],
        [0,-1,INF,INF]
    ]
    wallsAndGates(rooms)
    print(rooms)  # Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
