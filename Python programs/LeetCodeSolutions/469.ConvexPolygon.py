"""
469. Convex Polygon

Given a list of points that form a polygon, return true if the polygon is convex.

Constraints:
- 3 <= points.length <= 10^4
- points[i].length == 2
- -10^4 <= points[i][j] <= 10^4

Example:
Input: points = [[0,0],[0,1],[1,1],[1,0]]
Output: True
"""

class Solution:
    def isConvex(self, points: list) -> bool:
        def cross(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
        n = len(points)
        prev = 0
        for i in range(n):
            c = cross(points[i], points[(i+1)%n], points[(i+2)%n])
            if c != 0:
                if c * prev < 0:
                    return False
                prev = c
        return True

# Example usage:
sol = Solution()
print(sol.isConvex([[0,0],[0,1],[1,1],[1,0]]))  # Output: True
