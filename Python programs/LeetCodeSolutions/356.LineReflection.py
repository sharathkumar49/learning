"""
356. Line Reflection

Given n points on a 2D plane, check if there is a line parallel to the y-axis that reflects the given points symmetrically.

Constraints:
- 1 <= points.length <= 10^4
- points[i].length == 2
- -10^8 <= points[i][j] <= 10^8
"""
from typing import List

class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        points_set = set(map(tuple, points))
        min_x = min(x for x, y in points)
        max_x = max(x for x, y in points)
        line = (min_x + max_x) / 2
        for x, y in points:
            if (2 * line - x, y) not in points_set:
                return False
        return True

# Example usage:
points = [[1,1],[-1,1]]
print(Solution().isReflected(points))  # Output: True
