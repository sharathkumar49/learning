"""
452. Minimum Number of Arrows to Burst Balloons

Given a set of points that represent the start and end of balloons, find the minimum number of arrows that must be shot to burst all balloons.

Constraints:
- 1 <= points.length <= 10^5
- points[i].length == 2
- -2^31 <= x_start < x_end <= 2^31 - 1

Example:
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
"""

class Solution:
    def findMinArrowShots(self, points: list) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[1])
        arrows = 1
        end = points[0][1]
        for x, y in points[1:]:
            if x > end:
                arrows += 1
                end = y
        return arrows

# Example usage:
sol = Solution()
print(sol.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))  # Output: 2
