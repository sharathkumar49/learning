"""
LeetCode 1924. Erect the Fence II

Given a set of points, return the minimum perimeter fence that encloses all the points (convex hull).

Example:
Input: points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
Output: [[1,1],[2,0],[4,2],[3,3],[2,4]]

Constraints:
- 1 <= points.length <= 10^4
- points[i].length == 2
- 0 <= points[i][j] <= 10^4
"""

def outerTrees(points):
    points = sorted(map(tuple, points))
    def cross(o, a, b):
        return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
    hull = []
    for p in points:
        while len(hull) >= 2 and cross(hull[-2], hull[-1], p) < 0:
            hull.pop()
        hull.append(p)
    t = len(hull)
    for p in reversed(points):
        while len(hull) > t and cross(hull[-2], hull[-1], p) < 0:
            hull.pop()
        hull.append(p)
    return list(set(hull))

# Example usage:
# print(outerTrees([[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]))
