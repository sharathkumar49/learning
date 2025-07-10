"""
LeetCode 1923. Longest Common Subpath

Given n cities and an array of paths, return the length of the longest common subpath shared by all paths.

Example:
Input: n = 5, paths = [[0,1,2,3,4],[4,3,2,1,0]]
Output: 1

Constraints:
- 2 <= n <= 10^5
- 1 <= paths.length <= 10^5
- 1 <= paths[i].length <= 10^5
- sum(paths[i].length) <= 10^5
"""

def longestCommonSubpath(n, paths):
    import random
    MOD1, MOD2 = 10**11+19, 10**11+21
    BASE1, BASE2 = random.randint(10**5, 10**6), random.randint(10**5, 10**6)
    def check(L):
        hashes = None
        for path in paths:
            h1 = h2 = 0
            power1 = pow(BASE1, L, MOD1)
            power2 = pow(BASE2, L, MOD2)
            s = set()
            for i, x in enumerate(path):
                h1 = (h1 * BASE1 + x) % MOD1
                h2 = (h2 * BASE2 + x) % MOD2
                if i >= L:
                    h1 = (h1 - path[i-L] * power1) % MOD1
                    h2 = (h2 - path[i-L] * power2) % MOD2
                if i >= L-1:
                    s.add((h1, h2))
            if hashes is None:
                hashes = s
            else:
                hashes &= s
            if not hashes:
                return False
        return True
    left, right = 0, min(len(p) for p in paths)
    while left < right:
        mid = (left + right + 1) // 2
        if check(mid):
            left = mid
        else:
            right = mid - 1
    return left

# Example usage:
# print(longestCommonSubpath(5, [[0,1,2,3,4],[4,3,2,1,0]]))  # Output: 1
