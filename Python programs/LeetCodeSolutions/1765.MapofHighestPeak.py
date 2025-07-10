"""
LeetCode 1765. Map of Highest Peak

Given a matrix isWater, return a matrix of the same size where each cell is the height of the highest peak.

Example 1:
Input: isWater = [[0,1],[0,0]]
Output: [[1,0],[2,1]]

Constraints:
- 1 <= m, n <= 1000
- isWater[i][j] is 0 or 1
"""

def highestPeak(isWater):
    from collections import deque
    m, n = len(isWater), len(isWater[0])
    res = [[-1]*n for _ in range(m)]
    q = deque()
    for i in range(m):
        for j in range(n):
            if isWater[i][j]:
                res[i][j] = 0
                q.append((i, j))
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    while q:
        x, y = q.popleft()
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0<=nx<m and 0<=ny<n and res[nx][ny]==-1:
                res[nx][ny] = res[x][y] + 1
                q.append((nx, ny))
    return res

# Example usage:
# isWater = [[0,1],[0,0]]
# print(highestPeak(isWater))  # Output: [[1,0],[2,1]]
