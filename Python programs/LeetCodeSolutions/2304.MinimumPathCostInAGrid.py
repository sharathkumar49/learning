"""
LeetCode 2304. Minimum Path Cost in a Grid

Given grid and moveCost, return the minimum path cost from the first row to the last row.

Example:
Input: grid = [[5,3],[4,0],[2,1]], moveCost = [[9,4],[6,7],[1,5]]
Output: 9

Constraints:
- 2 <= grid.length, grid[0].length <= 100
"""

def minPathCost(grid, moveCost):
    m, n = len(grid), len(grid[0])
    dp = grid[0][:]
    for i in range(1, m):
        new_dp = [float('inf')]*n
        for j in range(n):
            for k in range(n):
                new_dp[j] = min(new_dp[j], dp[k] + moveCost[grid[i-1][k]][j] + grid[i][j])
        dp = new_dp
    return min(dp)

# Example usage:
# print(minPathCost([[5,3],[4,0],[2,1]], [[9,4],[6,7],[1,5]]))  # Output: 9
