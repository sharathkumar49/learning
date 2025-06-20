"""
LeetCode 711. Number of Distinct Islands II

Given a non-empty 2D grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical). You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated, rotated (90, 180, or 270 degrees), or reflected (left/right or up/down) to equal the other.

Example 1:
Input: grid = [[1,1,0,0,0],[1,0,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
Output: 1

Example 2:
Input: grid = [[1,1,1,0,0],[1,0,0,0,0],[1,1,0,0,1],[0,1,0,1,1]]
Output: 2

Constraints:
- 1 <= grid.length, grid[0].length <= 50
- grid[i][j] is either 0 or 1.
"""
from typing import List

def numDistinctIslands2(grid: List[List[int]]) -> int:
    def dfs(x, y, pos):
        grid[x][y] = 0
        pos.append((x, y))
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny]:
                dfs(nx, ny, pos)
    def normalize(shape):
        shapes = []
        for trans in [(1,1),(1,-1),(-1,1),(-1,-1)]:
            for swap in [False, True]:
                s = [(x*trans[0], y*trans[1]) for x, y in shape]
                if swap:
                    s = [(y, x) for x, y in s]
                minx = min(x for x, y in s)
                miny = min(y for x, y in s)
                s = sorted((x-minx, y-miny) for x, y in s)
                shapes.append(tuple(s))
        return min(shapes)
    seen = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                pos = []
                dfs(i, j, pos)
                seen.add(normalize(pos))
    return len(seen)

# Example usage
if __name__ == "__main__":
    print(numDistinctIslands2([[1,1,0,0,0],[1,0,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))  # Output: 1
    print(numDistinctIslands2([[1,1,1,0,0],[1,0,0,0,0],[1,1,0,0,1],[0,1,0,1,1]]))  # Output: 2
