"""
514. Freedom Trail

Given a string ring and a string key, return the minimum number of steps to spell all the characters in key by rotating the ring and pressing the center button.

Constraints:
- 1 <= ring.length, key.length <= 100
- ring and key consist of only lowercase English letters.
- It is guaranteed that key could always be spelled by rotating the ring.

Example:
Input: ring = "godding", key = "gd"
Output: 4
"""

from collections import defaultdict

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        pos = defaultdict(list)
        for i, c in enumerate(ring):
            pos[c].append(i)
        memo = {}
        def dp(i, j):
            if j == len(key):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            res = float('inf')
            for k in pos[key[j]]:
                diff = abs(i - k)
                step = min(diff, n - diff)
                res = min(res, step + 1 + dp(k, j+1))
            memo[(i, j)] = res
            return res
        return dp(0, 0)

# Example usage:
sol = Solution()
print(sol.findRotateSteps("godding", "gd"))  # Output: 4
