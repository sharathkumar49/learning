"""
973. K Closest Points to Origin
https://leetcode.com/problems/k-closest-points-to-origin/

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

Constraints:
- 1 <= k <= points.length <= 10^4
- -10^4 <= xi, yi <= 10^4

Example:
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
"""
from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return heapq.nsmallest(k, points, key=lambda x: x[0]**2 + x[1]**2)

# Example usage
if __name__ == "__main__":
    points = [[1,3],[-2,2]]
    k = 1
    print(Solution().kClosest(points, k))  # Output: [[-2,2]]
