"""
LeetCode 1828. Queries on Number of Points Inside a Circle

Given points and queries (each query is a circle), return the number of points inside each circle.

Example 1:
Input: points = [[1,1],[2,2],[3,3],[4,4],[5,5]], queries = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]
Output: [2,3,2,4]

Constraints:
- 1 <= points.length <= 500
- 1 <= queries.length <= 500
- 0 <= x, y, xj, yj <= 500
- 1 <= rj <= 500
"""

def countPoints(points, queries):
    res = []
    for x, y, r in queries:
        cnt = 0
        for px, py in points:
            if (px-x)**2 + (py-y)**2 <= r*r:
                cnt += 1
        res.append(cnt)
    return res

# Example usage:
# points = [[1,1],[2,2],[3,3],[4,4],[5,5]]
# queries = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]
# print(countPoints(points, queries))  # Output: [2,3,2,4]
