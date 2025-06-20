"""
939. Minimum Area Rectangle
https://leetcode.com/problems/minimum-area-rectangle/

Given an array of points in the X-Y plane, return the minimum area of a rectangle formed from these points, with sides parallel to the axes. If no rectangle can be formed, return 0.

Constraints:
- 1 <= points.length <= 500
- points[i].length == 2
- 0 <= points[i][j] <= 4 * 10^4
- All the given points are unique.

Example:
Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
"""
from typing import List

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        point_set = set(map(tuple, points))
        min_area = float('inf')
        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 != x2 and y1 != y2:
                    if (x1, y2) in point_set and (x2, y1) in point_set:
                        min_area = min(min_area, abs(x1-x2)*abs(y1-y2))
        return 0 if min_area == float('inf') else min_area

# Example usage
if __name__ == "__main__":
    points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
    print(Solution().minAreaRect(points))  # Output: 4
