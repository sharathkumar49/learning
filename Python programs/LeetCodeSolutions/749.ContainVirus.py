"""
LeetCode 749. Contain Virus

A virus is spreading rapidly, and your task is to contain it by building walls.
Given a 2D grid, each cell is either 0 (uninfected), 1 (infected), or -1 (wall).
Return the minimum number of walls required to contain the virus.

Example 1:
Input: isInfected = [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]
Output: 10

Example 2:
Input: isInfected = [[1,1,1],[1,0,1],[1,1,1]]
Output: 4

Constraints:
- m == isInfected.length
- n == isInfected[i].length
- 1 <= m, n <= 50
- isInfected[i][j] is either 0, 1, or -1.
"""
from typing import List

def containVirus(isInfected: List[List[int]]) -> int:
    m, n = len(isInfected), len(isInfected[0])
    res = 0
    while True:
        seen = set()
        regions = []
        fronts = []
        walls = []
        for i in range(m):
            for j in range(n):
                if isInfected[i][j] == 1 and (i, j) not in seen:
                    stack = [(i, j)]
                    region = set()
                    front = set()
                    wall = 0
                    while stack:
                        x, y = stack.pop()
                        if (x, y) in seen:
                            continue
                        seen.add((x, y))
                        region.add((x, y))
                        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                            nx, ny = x+dx, y+dy
                            if 0<=nx<m and 0<=ny<n:
                                if isInfected[nx][ny] == 0:
                                    front.add((nx, ny))
                                    wall += 1
                                elif isInfected[nx][ny] == 1 and (nx, ny) not in seen:
                                    stack.append((nx, ny))
                    regions.append(region)
                    fronts.append(front)
                    walls.append(wall)
        if not regions:
            break
        idx = 0
        for i in range(1, len(fronts)):
            if len(fronts[i]) > len(fronts[idx]):
                idx = i
        res += walls[idx]
        for i, region in enumerate(regions):
            if i == idx:
                for x, y in region:
                    isInfected[x][y] = -1
            else:
                for x, y in fronts[i]:
                    isInfected[x][y] = 1
        if sum(walls) == 0:
            break
    return res

# Example usage
if __name__ == "__main__":
    print(containVirus([[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]))  # Output: 10
    print(containVirus([[1,1,1],[1,0,1],[1,1,1]]))  # Output: 4
