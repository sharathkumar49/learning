"""
LeetCode 1266. Minimum Time Visiting All Points

On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in seconds to visit all the points in order. You can move in 8 directions (horizontal, vertical, diagonal) in 1 second per move.

Constraints:
- points.length == n
- 1 <= n <= 100
- points[i].length == 2
- -1000 <= points[i][0], points[i][1] <= 1000

Example:
Input: points = [[1,1],[3,4],[-1,0]]
Output: 7

"""
def minTimeToVisitAllPoints(points):
    time = 0
    for i in range(1, len(points)):
        x1, y1 = points[i-1]
        x2, y2 = points[i]
        time += max(abs(x2-x1), abs(y2-y1))
    return time

# Example usage:
points = [[1,1],[3,4],[-1,0]]
print(minTimeToVisitAllPoints(points))  # Output: 7
