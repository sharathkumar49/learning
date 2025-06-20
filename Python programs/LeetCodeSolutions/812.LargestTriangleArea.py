"""
812. Largest Triangle Area

Given a list of points in the plane, return the area of the largest triangle that can be formed by any 3 of the points.

Example 1:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2.0

Constraints:
- 3 <= points.length <= 50
- -50 <= points[i][j] <= 50
- All points are unique.
"""
def largestTriangleArea(points):
    def area(a, b, c):
        return abs((a[0]*(b[1]-c[1]) + b[0]*(c[1]-a[1]) + c[0]*(a[1]-b[1])) / 2)
    n = len(points)
    max_area = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                max_area = max(max_area, area(points[i], points[j], points[k]))
    return max_area

# Example usage:
print(largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]]))  # Output: 2.0
