"""
LeetCode 1610. Maximum Number of Visible Points

Given a list of points on a 2D plane and an integer angle, return the maximum number of points that can be seen from a fixed location within a viewing angle.

Example 1:
Input: points = [[2,1],[2,2],[3,3]], angle = 90, location = [1,1]
Output: 3

Constraints:
- 1 <= points.length <= 10^5
- points[i].length == 2
- location.length == 2
- 0 <= angle < 360
- 0 <= points[i][j], location[j] <= 10^9
"""

import math

def visiblePoints(points, angle, location):
    same = 0
    angles = []
    x0, y0 = location
    for x, y in points:
        if x == x0 and y == y0:
            same += 1
        else:
            angles.append(math.atan2(y - y0, x - x0) * 180 / math.pi)
    angles.sort()
    n = len(angles)
    angles += [a + 360 for a in angles]
    res = i = 0
    for j in range(len(angles)):
        while angles[j] - angles[i] > angle:
            i += 1
        res = max(res, j - i + 1)
    return res + same

# Example usage:
# points = [[2,1],[2,2],[3,3]]
# angle = 90
# location = [1,1]
# print(visiblePoints(points, angle, location))  # Output: 3
