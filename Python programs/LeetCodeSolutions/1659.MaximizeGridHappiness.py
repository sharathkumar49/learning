"""
LeetCode 1659. Maximize Grid Happiness

Given m, n, introvertsCount, and extrovertsCount, return the maximum total happiness of the grid.

Example 1:
Input: m = 2, n = 3, introvertsCount = 1, extrovertsCount = 2
Output: 240

Constraints:
- 1 <= m, n <= 5
- 0 <= introvertsCount, extrovertsCount <= m * n
"""

def getMaxGridHappiness(m, n, introvertsCount, extrovertsCount):
    from functools import lru_cache
    dirs = [(-1,0),(0,-1)]
    @lru_cache(None)
    def dfs(pos, mask, intro, extro):
        if pos == m*n or (intro == 0 and extro == 0):
            return 0
        res = dfs(pos+1, (mask*3)% (3**n), intro, extro)
        i, j = divmod(pos, n)
        for t, cnt, base, delta in ((1, intro, 120, -30), (2, extro, 40, 20)):
            if cnt:
                happy = base
                for d, (di, dj) in enumerate(dirs):
                    ni, nj = i+di, j+dj
                    if 0<=ni<m and 0<=nj<n:
                        p = (mask // (3**nj)) % 3
                        if p:
                            happy += delta if t == 1 else -delta
                            happy += -30 if p == 1 and t == 1 else 20 if p == 2 and t == 1 else 20 if p == 1 and t == 2 else -30 if p == 2 and t == 2 else 0
                nmask = mask + t * (3**j)
                res = max(res, happy + dfs(pos+1, nmask % (3**n), intro-(t==1), extro-(t==2)))
        return res
    return dfs(0, 0, introvertsCount, extrovertsCount)

# Example usage:
# m = 2
# n = 3
# introvertsCount = 1
# extrovertsCount = 2
# print(getMaxGridHappiness(m, n, introvertsCount, extrovertsCount))  # Output: 240
