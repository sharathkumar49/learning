"""
LeetCode 1779. Find Nearest Point That Has the Same X or Y Coordinate

Given coordinates x and y, and a list of points, return the index of the nearest valid point (same x or y), or -1 if none exists.

Example 1:
Input: x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
Output: 2

Constraints:
- 1 <= points.length <= 10^4
- points[i].length == 2
- 1 <= x, y, points[i][j] <= 10^4
"""

def nearestValidPoint(x, y, points):
    res = -1
    min_dist = float('inf')
    for i, (a, b) in enumerate(points):
        if a == x or b == y:
            dist = abs(x - a) + abs(y - b)
            if dist < min_dist:
                min_dist = dist
                res = i
    return res

# Example usage:
# x = 3
# y = 4
# points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
# print(nearestValidPoint(x, y, points))  # Output: 2
