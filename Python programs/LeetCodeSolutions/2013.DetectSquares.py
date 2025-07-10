"""
LeetCode 2013. Detect Squares

Design a data structure that supports adding points and counting the number of squares with a given point as one of the corners.

Example:
Input: ["DetectSquares","add","add","add","count"], [[],[3,10],[11,2],[3,2],[11,10]]
Output: [null,null,null,null,1]

Constraints:
- add and count will be called at most 5000 times.
- 0 <= x, y <= 1000
"""

class DetectSquares:
    def __init__(self):
        from collections import Counter
        self.points = Counter()
        self.x_points = {}

    def add(self, point):
        x, y = point
        self.points[(x, y)] += 1
        if x not in self.x_points:
            self.x_points[x] = set()
        self.x_points[x].add(y)

    def count(self, point):
        x, y = point
        res = 0
        if x not in self.x_points:
            return 0
        for col_y in self.x_points[x]:
            if col_y == y:
                continue
            d = abs(col_y - y)
            for nx in [x - d, x + d]:
                res += self.points[(nx, y)] * self.points[(nx, col_y)] * self.points[(x, col_y)]
        return res

# Example usage:
# ds = DetectSquares()
# ds.add([3,10])
# ds.add([11,2])
# ds.add([3,2])
# print(ds.count([11,10]))  # Output: 1
