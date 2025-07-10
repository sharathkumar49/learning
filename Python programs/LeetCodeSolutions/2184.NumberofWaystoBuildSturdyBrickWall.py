"""
LeetCode 2184. Number of Ways to Build Sturdy Brick Wall

Given n, m, and an array of allowed brick lengths, return the number of ways to build a wall of width m and height n such that no two vertical joints line up in adjacent rows.

Example:
Input: n = 2, m = 3, bricks = [1,2]
Output: 2

Constraints:
- 1 <= n, m <= 10
- 1 <= bricks.length <= 10
- 1 <= bricks[i] <= m
"""

def buildWall(n, m, bricks):
    from functools import lru_cache
    def get_masks(m, bricks):
        res = set()
        def dfs(pos, mask):
            if pos == m:
                res.add(mask)
                return
            for b in bricks:
                if pos + b <= m:
                    dfs(pos + b, mask | (1 << (pos + b)))
        dfs(0, 0)
        return res
    masks = get_masks(m, bricks)
    @lru_cache(None)
    def dp(row, prev):
        if row == n:
            return 1
        return sum(dp(row+1, mask) for mask in masks if mask & prev == 0)
    return dp(0, 0)

# Example usage:
# print(buildWall(2, 3, [1,2]))  # Output: 2
