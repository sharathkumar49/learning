"""
LeetCode 2061. Number of Spaces Cleaning Robot Cleaned

Given a grid and a robot's movement, return the number of unique spaces the robot cleaned.

Example:
Input: room = [[1,1,1],[1,0,1],[1,1,1]], moves = "RRDDLLUU"
Output: 8

Constraints:
- 1 <= room.length, room[0].length <= 100
- 0 <= room[i][j] <= 1
"""

def numberOfCleanedSpaces(room, moves):
    m, n = len(room), len(room[0])
    x = y = 0
    cleaned = set([(x, y)])
    dirs = {'U': (-1,0), 'D': (1,0), 'L': (0,-1), 'R': (0,1)}
    for move in moves:
        dx, dy = dirs[move]
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n and room[nx][ny] == 1:
            x, y = nx, ny
            cleaned.add((x, y))
    return len(cleaned)

# Example usage:
# print(numberOfCleanedSpaces([[1,1,1],[1,0,1],[1,1,1]], "RRDDLLUU"))  # Output: 8
