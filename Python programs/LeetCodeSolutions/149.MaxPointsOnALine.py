"""
149. Max Points on a Line
https://leetcode.com/problems/max-points-on-a-line/

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

Constraints:
- 1 <= points.length <= 300
- points[i].length == 2
- -10^4 <= xi, yi <= 10^4
- All the points are unique.

Example:
Input: points = [[1,1],[2,2],[3,3]]
Output: 3
"""
from typing import List
from collections import defaultdict

def maxPoints(points: List[List[int]]) -> int:
    if len(points) <= 2:
        return len(points)
    result = 0
    for i in range(len(points)):
        slopes = defaultdict(int)
        duplicates = 1
        for j in range(i+1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]
            if x1 == x2 and y1 == y2:
                duplicates += 1
            elif x1 == x2:
                slopes['inf'] += 1
            else:
                slope = (y2 - y1) / (x2 - x1)
                slopes[slope] += 1
        result = max(result, duplicates + (max(slopes.values()) if slopes else 0))
    return result

# Example usage:
if __name__ == "__main__":
    print(maxPoints([[1,1],[2,2],[3,3]]))  # Output: 3
    print(maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))  # Output: 4
