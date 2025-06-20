"""
963. Minimum Area Rectangle II
https://leetcode.com/problems/minimum-area-rectangle-ii/

Given a set of points in the xy-plane, return the minimum area of any rectangle formed from these points, with sides not necessarily parallel to the axes. If there isn't any rectangle, return 0.

Constraints:
- 1 <= points.length <= 50
- points[i].length == 2
- 0 <= points[i][j] <= 4 * 10^4
- All the given points are unique.

Example:
Input: points = [[1,2],[2,1],[1,0],[0,1]]
Output: 2.0
"""
from typing import List
from collections import defaultdict

class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        import math
        point_set = set(map(tuple, points))
        n = len(points)
        min_area = float('inf')
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j and i != k and j != k:
                        x1, y1 = points[i]
                        x2, y2 = points[j]
                        x3, y3 = points[k]
                        dx1, dy1 = x2 - x1, y2 - y1
                        dx2, dy2 = x3 - x1, y3 - y1
                        if dx1 * dx2 + dy1 * dy2 == 0:
                            x4, y4 = x2 + dx2, y2 + dy2
                            if (x4, y4) in point_set:
                                area = math.hypot(dx1, dy1) * math.hypot(dx2, dy2)
                                if area < min_area and area > 0:
                                    min_area = area
        return 0 if min_area == float('inf') else min_area

# Example usage
if __name__ == "__main__":
    points = [[1,2],[2,1],[1,0],[0,1]]
    print(Solution().minAreaFreeRect(points))  # Output: 2.0
