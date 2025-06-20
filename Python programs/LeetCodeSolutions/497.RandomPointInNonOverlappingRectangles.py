"""
497. Random Point in Non-overlapping Rectangles

Given a list of non-overlapping axis-aligned rectangles, write a function pick which randomly and uniformly picks an integer point in the space covered by the rectangles.

Constraints:
- 1 <= rects.length <= 100
- rects[i].length == 4
- -10^9 <= rects[i][j] <= 10^9
- The rectangles are non-overlapping.

Example:
Input: rects = [[1,1,5,5]]
Output: [4,1]
"""

import random
import bisect

class Solution:
    def __init__(self, rects: list):
        self.rects = rects
        self.areas = []
        area = 0
        for x1, y1, x2, y2 in rects:
            area += (x2 - x1 + 1) * (y2 - y1 + 1)
            self.areas.append(area)
    def pick(self) -> list:
        k = random.randint(1, self.areas[-1])
        idx = bisect.bisect_left(self.areas, k)
        x1, y1, x2, y2 = self.rects[idx]
        w = x2 - x1 + 1
        h = y2 - y1 + 1
        base = self.areas[idx-1] if idx > 0 else 0
        offset = k - base - 1
        return [x1 + offset % w, y1 + offset // w]

# Example usage:
sol = Solution([[1,1,5,5]])
print(sol.pick())  # Output: e.g. [4, 1]
