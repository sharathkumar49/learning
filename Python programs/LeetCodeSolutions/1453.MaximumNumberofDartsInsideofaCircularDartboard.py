"""
LeetCode 1453. Maximum Number of Darts Inside of a Circular Dartboard

You have a very large square dartboard, and a list of points on the dartboard. Each point is represented as a pair [x, y].

Return the maximum number of points that can be enclosed by a circle of radius r.

Constraints:
- 1 <= points.length <= 100
- points[i].length == 2
- 1 <= points[i][0], points[i][1] <= 100
- 1 <= r <= 100

Example:
Input: points = [[-2,0],[2,0],[0,2],[0,-2]], r = 2
Output: 4
"""
import math

def numPoints(points, r):
    def dist(p1, p2):
        return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

    n = len(points)
    res = 1
    for i in range(n):
        for j in range(i + 1, n):
            d = dist(points[i], points[j])
            if d > 2 * r:
                continue
            midx = (points[i][0] + points[j][0]) / 2
            midy = (points[i][1] + points[j][1]) / 2
            angle = math.atan2(points[j][1] - points[i][1], points[j][0] - points[i][0])
            h = math.sqrt(r * r - (d / 2) ** 2)
            dx = h * math.sin(angle)
            dy = -h * math.cos(angle)
            for sign in [1, -1]:
                cx = midx + sign * dx
                cy = midy + sign * dy
                count = 0
                for k in range(n):
                    if dist([cx, cy], points[k]) <= r + 1e-8:
                        count += 1
                res = max(res, count)
    return res

# Example usage:
points = [[-2,0],[2,0],[0,2],[0,-2]]
r = 2
print(numPoints(points, r))  # Output: 4
