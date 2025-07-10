"""
LeetCode 2152. Minimum Number of Lines to Cover Points

Given a 2D integer array points, return the minimum number of straight lines needed to cover all the points.

Example:
Input: points = [[1,1],[2,2],[3,3],[4,1]]
Output: 2

Constraints:
- 1 <= points.length <= 10
- points[i].length == 2
- -10^9 <= points[i][j] <= 10^9
"""

def minLines(points):
    from math import gcd
    n = len(points)
    if n <= 2:
        return 1
    points = [tuple(p) for p in points]
    memo = {}
    def dfs(mask):
        if mask == 0:
            return 0
        if mask in memo:
            return memo[mask]
        res = n
        first = 0
        while not (mask & (1<<first)):
            first += 1
        for j in range(n):
            if j == first or not (mask & (1<<j)):
                continue
            dx = points[j][0] - points[first][0]
            dy = points[j][1] - points[first][1]
            g = gcd(dx, dy)
            dx //= g
            dy //= g
            new_mask = mask
            for k in range(n):
                if not (mask & (1<<k)):
                    continue
                if (points[k][0] - points[first][0]) * dy == (points[k][1] - points[first][1]) * dx:
                    new_mask &= ~(1<<k)
            res = min(res, 1 + dfs(new_mask))
        memo[mask] = res
        return res
    return dfs((1<<n)-1)

# Example usage:
# print(minLines([[1,1],[2,2],[3,3],[4,1]]))  # Output: 2
