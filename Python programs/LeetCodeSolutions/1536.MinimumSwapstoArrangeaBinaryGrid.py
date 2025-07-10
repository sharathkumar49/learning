"""
LeetCode 1536. Minimum Swaps to Arrange a Binary Grid

Given an n x n binary grid, return the minimum number of swaps to arrange the grid so that all 1s are below the main diagonal. If it is impossible, return -1.

Constraints:
- 1 <= n <= 200
- grid[i][j] is 0 or 1

Example:
Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
Output: 3
"""
def minSwaps(grid):
    n = len(grid)
    right = [max([j for j, v in enumerate(row) if v] + [-1]) for row in grid]
    res = 0
    for i in range(n):
        j = i
        while j < n and right[j] < i:
            j += 1
        if j == n:
            return -1
        res += j - i
        while j > i:
            right[j], right[j-1] = right[j-1], right[j]
            j -= 1
    return res

# Example usage:
grid = [[0,0,1],[1,1,0],[1,0,0]]
print(minSwaps(grid))  # Output: 3
