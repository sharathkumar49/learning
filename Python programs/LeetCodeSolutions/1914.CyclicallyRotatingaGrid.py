"""
LeetCode 1914. Cyclically Rotating a Grid

Given an m x n integer matrix grid and an integer k, cyclically rotate each layer of the grid k times.

Example:
Input: grid = [[40,10],[30,20]], k = 1
Output: [[10,20],[40,30]]

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 50
- 1 <= grid[i][j] <= 10^5
- 1 <= k <= 10^9
"""

def rotateGrid(grid, k):
    m, n = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    for layer in range(min(m, n)//2):
        vals = []
        for j in range(layer, n-layer): vals.append(grid[layer][j])
        for i in range(layer+1, m-layer): vals.append(grid[i][n-layer-1])
        for j in range(n-layer-2, layer-1, -1): vals.append(grid[m-layer-1][j])
        for i in range(m-layer-2, layer, -1): vals.append(grid[i][layer])
        l = len(vals)
        vals = vals[k%l:] + vals[:k%l]
        idx = 0
        for j in range(layer, n-layer): res[layer][j] = vals[idx]; idx += 1
        for i in range(layer+1, m-layer): res[i][n-layer-1] = vals[idx]; idx += 1
        for j in range(n-layer-2, layer-1, -1): res[m-layer-1][j] = vals[idx]; idx += 1
        for i in range(m-layer-2, layer, -1): res[i][layer] = vals[idx]; idx += 1
    return res

# Example usage:
# print(rotateGrid([[40,10],[30,20]], 1))  # Output: [[10,20],[40,30]]
