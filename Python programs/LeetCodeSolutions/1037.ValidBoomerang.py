"""
1037. Valid Boomerang

Given three points in a plane, return true if and only if they form a boomerang (i.e., they are all distinct and not in a straight line).

Constraints:
- points.length == 3
- points[i].length == 2
- 0 <= points[i][j] <= 100

Example:
Input: points = [[1,1],[2,3],[3,2]]
Output: true
"""
from typing import List

def isBoomerang(points: List[List[int]]) -> bool:
    (x1, y1), (x2, y2), (x3, y3) = points
    return (x2 - x1)*(y3 - y1) != (y2 - y1)*(x3 - x1) and len({tuple(p) for p in points}) == 3

# Example usage:
points = [[1,1],[2,3],[3,2]]
print(isBoomerang(points))  # Output: True
