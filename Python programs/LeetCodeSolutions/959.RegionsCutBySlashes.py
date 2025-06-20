"""
959. Regions Cut By Slashes
https://leetcode.com/problems/regions-cut-by-slashes/

Given an n x n grid, each cell is either '/', '\\', or ' '. Return the number of regions cut by slashes.

Constraints:
- 1 <= n <= 30
- grid[i].length == n
- grid[i][j] is either '/', '\\', or ' '

Example:
Input: grid = [" /","/ "]
Output: 2
"""
from typing import List

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        parent = [i for i in range(4*n*n)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            parent[find(x)] = find(y)
        for i in range(n):
            for j in range(n):
                idx = 4 * (i * n + j)
                c = grid[i][j]
                if c == ' ':
                    union(idx+0, idx+1)
                    union(idx+1, idx+2)
                    union(idx+2, idx+3)
                elif c == '/':
                    union(idx+0, idx+3)
                    union(idx+1, idx+2)
                else:  # '\\'
                    union(idx+0, idx+1)
                    union(idx+2, idx+3)
                if i+1 < n:
                    union(idx+2, 4*((i+1)*n+j)+0)
                if j+1 < n:
                    union(idx+1, 4*(i*n+j+1)+3)
        return sum(i == find(i) for i in range(4*n*n))

# Example usage
if __name__ == "__main__":
    grid = [" /","/ "]
    print(Solution().regionsBySlashes(grid))  # Output: 2
