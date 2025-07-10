"""
LeetCode 1459. Find All Groups of Farmland

Given a 2D binary matrix land where 0 represents uncultivated land and 1 represents farmland, return a list of the coordinates of the top left and bottom right corner of each group of farmland.

Constraints:
- m == land.length
- n == land[i].length
- 1 <= m, n <= 300
- land[i][j] is 0 or 1.

Example:
Input: land = [[1,0,0],[0,1,1],[0,1,1]]
Output: [[0,0,0,0],[1,1,2,2]]
"""
def findFarmland(land):
    m, n = len(land), len(land[0])
    res = []
    visited = [[False]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if land[i][j] == 1 and not visited[i][j]:
                x, y = i, j
                while x+1 < m and land[x+1][j] == 1:
                    x += 1
                while y+1 < n and land[i][y+1] == 1:
                    y += 1
                for a in range(i, x+1):
                    for b in range(j, y+1):
                        visited[a][b] = True
                res.append([i, j, x, y])
    return res

# Example usage:
land = [[1,0,0],[0,1,1],[0,1,1]]
print(findFarmland(land))  # Output: [[0,0,0,0],[1,1,2,2]]
