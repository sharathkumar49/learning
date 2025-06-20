"""
447. Number of Boomerangs

Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).
Return the number of boomerangs.

Constraints:
- n == points.length
- 1 <= n <= 500
- points[i].length == 2
- -10^4 <= x_i, y_i <= 10^4

Example:
Input: points = [[0,0],[1,0],[2,0]]
Output: 2
"""

from collections import defaultdict

class Solution:
    def numberOfBoomerangs(self, points: list) -> int:
        res = 0
        for i in points:
            d = defaultdict(int)
            for j in points:
                dist = (i[0]-j[0])**2 + (i[1]-j[1])**2
                d[dist] += 1
            for v in d.values():
                res += v * (v-1)
        return res

# Example usage:
sol = Solution()
print(sol.numberOfBoomerangs([[0,0],[1,0],[2,0]]))  # Output: 2
