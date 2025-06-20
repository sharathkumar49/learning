"""
LeetCode 694. Number of Distinct Islands

Given a non-empty 2D grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical). You may assume all four edges of the grid are surrounded by water.
Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (not rotated or reflected) to equal the other.

Example 1:
Input: grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
Output: 1

Example 2:
Input: grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
Output: 3

Constraints:
- 1 <= grid.length, grid[0].length <= 50
- grid[i][j] is either 0 or 1.
"""
from typing import List

def numDistinctIslands(grid: List[List[int]]) -> int:
    def dfs(x, y, direction):
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y]:
            grid[x][y] = 0
            path = direction
            path += dfs(x+1, y, 'd')
            path += dfs(x-1, y, 'u')
            path += dfs(x, y+1, 'r')
            path += dfs(x, y-1, 'l')
            path += 'b'
            return path
        return ''
    shapes = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                shape = dfs(i, j, 'o')
                shapes.add(shape)
    return len(shapes)

# Example usage
if __name__ == "__main__":
    print(numDistinctIslands([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))  # Output: 1
    print(numDistinctIslands([[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]))  # Output: 3
