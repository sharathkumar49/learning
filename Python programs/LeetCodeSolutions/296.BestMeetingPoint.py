"""
296. Best Meeting Point

A group of two or more people wants to meet and minimize the total travel distance. You are given an m x n binary grid where each 1 marks the home of someone in the group. Return the minimal total travel distance.

The total travel distance is the sum of the distances between the houses of the people and the meeting point. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 200
- grid[i][j] is either 0 or 1.
- There will be at least two people in the group.
"""
from typing import List

class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        rows = [i for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 1]
        cols = [j for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 1]
        cols.sort()
        def minDist(points):
            i, j = 0, len(points) - 1
            dist = 0
            while i < j:
                dist += points[j] - points[i]
                i += 1
                j -= 1
            return dist
        return minDist(rows) + minDist(cols)

# Example usage:
grid = [
    [1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0]
]
print(Solution().minTotalDistance(grid))  # Output: 6
