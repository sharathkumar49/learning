"""
LeetCode 2250. Count Number of Rectangles Containing Each Point

Given rectangles and points, return the number of rectangles containing each point.

Example:
Input: rectangles = [[1,2],[2,3],[3,4]], points = [[1,3],[3,1]]
Output: [1,3]

Constraints:
- 1 <= rectangles.length, points.length <= 10^5
- 1 <= rectangles[i][0], rectangles[i][1], points[i][0], points[i][1] <= 10^9
"""

def countRectangles(rectangles, points):
    rectangles.sort()
    res = []
    for x, y in points:
        cnt = 0
        for rx, ry in rectangles:
            if rx >= x and ry >= y:
                cnt += 1
        res.append(cnt)
    return res

# Example usage:
# print(countRectangles([[1,2],[2,3],[3,4]], [[1,3],[3,1]]))  # Output: [1,3]
