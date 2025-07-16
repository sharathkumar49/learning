"""
LeetCode 2267. Check if There Is a Valid Parenthesis String Path

Given a grid, return true if there is a valid parenthesis string path from top-left to bottom-right.

Example:
Input: grid = [["(",")"],["(",")"]]
Output: True

Constraints:
- 1 <= grid.length, grid[0].length <= 100
"""

def hasValidPath(grid):
    m, n = len(grid), len(grid[0])
    from functools import lru_cache
    @lru_cache(None)
    def dfs(i, j, bal):
        if i >= m or j >= n or bal < 0:
            return False
        if i == m-1 and j == n-1:
            return bal == (1 if grid[i][j] == '(' else -1)
        if grid[i][j] == '(': bal += 1
        else: bal -= 1
        return dfs(i+1, j, bal) or dfs(i, j+1, bal)
    return dfs(0, 0, 0)

# Example usage:
# print(hasValidPath([["(",")"],["(",")"]]))  # Output: True
