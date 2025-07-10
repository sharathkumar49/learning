"""
LeetCode 1992. Find All Groups of Farmland

Given a binary matrix land, return the coordinates of all groups of farmland.

Example:
Input: land = [[1,0,0],[0,1,1],[0,1,1]]
Output: [[0,0,0,0],[1,1,2,2]]

Constraints:
- m == land.length
- n == land[i].length
- 1 <= m, n <= 300
- land[i][j] is 0 or 1
"""

def findFarmland(land):
    m, n = len(land), len(land[0])
    res = []
    for i in range(m):
        for j in range(n):
            if land[i][j] == 1:
                x, y = i, j
                while x+1 < m and land[x+1][j] == 1:
                    x += 1
                while y+1 < n and land[i][y+1] == 1:
                    y += 1
                res.append([i, j, x, y])
                for a in range(i, x+1):
                    for b in range(j, y+1):
                        land[a][b] = 0
    return res

# Example usage:
# print(findFarmland([[1,0,0],[0,1,1],[0,1,1]]))  # Output: [[0,0,0,0],[1,1,2,2]]
