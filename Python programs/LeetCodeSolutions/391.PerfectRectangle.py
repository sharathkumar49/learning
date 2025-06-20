"""
391. Perfect Rectangle

Given an array rectangles where rectangles[i] = [x1, y1, x2, y2] represents an axis-aligned rectangle, return true if they form a perfect rectangle.

Constraints:
- 1 <= rectangles.length <= 2 * 10^4
- rectangles[i].length == 4
- -10^5 <= x1 < x2 <= 10^5
- -10^5 <= y1 < y2 <= 10^5
"""
from typing import List

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area = 0
        corners = set()
        x1 = y1 = float('inf')
        x2 = y2 = float('-inf')
        for rec in rectangles:
            a, b, c, d = rec
            area += (c - a) * (d - b)
            x1, y1 = min(x1, a), min(y1, b)
            x2, y2 = max(x2, c), max(y2, d)
            for p in [(a, b), (a, d), (c, b), (c, d)]:
                if p in corners:
                    corners.remove(p)
                else:
                    corners.add(p)
        return area == (x2 - x1) * (y2 - y1) and len(corners) == 4 and (x1, y1) in corners and (x1, y2) in corners and (x2, y1) in corners and (x2, y2) in corners

# Example usage:
rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
print(Solution().isRectangleCover(rectangles))  # Output: True
