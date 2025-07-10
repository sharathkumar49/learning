"""
LeetCode 2087. Minimum Cost Homecoming of a Robot in a Grid

Given a grid, start and end positions, return the minimum cost for a robot to reach home.

Example:
Input: startPos = [1,0], homePos = [2,3], rowCosts = [5,4,3], colCosts = [8,2,6,7]
Output: 18

Constraints:
- 1 <= rowCosts.length, colCosts.length <= 10^5
- 0 <= startPos[i], homePos[i] < rowCosts.length/colCosts.length
"""

def minCost(startPos, homePos, rowCosts, colCosts):
    r1, c1 = startPos
    r2, c2 = homePos
    res = 0
    for r in range(r1, r2, 1 if r2 > r1 else -1):
        res += rowCosts[r + (1 if r2 > r1 else -1)]
    for c in range(c1, c2, 1 if c2 > c1 else -1):
        res += colCosts[c + (1 if c2 > c1 else -1)]
    return res

# Example usage:
# print(minCost([1,0], [2,3], [5,4,3], [8,2,6,7]))  # Output: 18
