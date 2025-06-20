"""
943. Find the Shortest Superstring
https://leetcode.com/problems/find-the-shortest-superstring/

Given an array of strings words, return the shortest string that has all the strings in words as substrings. If there are multiple valid answers, return any of them.

Constraints:
- 1 <= words.length <= 12
- 1 <= words[i].length <= 20
- words[i] consists only of lowercase English letters.

Example:
Input: words = ["alex","loves","leetcode"]
Output: "alexlovesleetcode"
"""
from typing import List

class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)
        overlaps = [[0]*n for _ in range(n)]
        for i, x in enumerate(words):
            for j, y in enumerate(words):
                if i != j:
                    for k in range(min(len(x), len(y)), 0, -1):
                        if x[-k:] == y[:k]:
                            overlaps[i][j] = k
                            break
        dp = [[0]*n for _ in range(1<<n)]
        parent = [[-1]*n for _ in range(1<<n)]
        for mask in range(1, 1<<n):
            for j in range(n):
                if not (mask & (1<<j)):
                    continue
                pmask = mask ^ (1<<j)
                if pmask == 0:
                    continue
                for i in range(n):
                    if not (pmask & (1<<i)):
                        continue
                    val = dp[pmask][i] + overlaps[i][j]
                    if val > dp[mask][j]:
                        dp[mask][j] = val
                        parent[mask][j] = i
        mask = (1<<n) - 1
        i = max(range(n), key=lambda j: dp[mask][j])
        perm = []
        while i != -1:
            perm.append(i)
            next_i = parent[mask][i]
            mask ^= (1<<i)
            i = next_i
        perm = perm[::-1]
        seen = set(perm)
        for j in range(n):
            if j not in seen:
                perm.append(j)
        res = words[perm[0]]
        for k in range(1, len(perm)):
            i, j = perm[k-1], perm[k]
            res += words[j][overlaps[i][j]:]
        return res

# Example usage
if __name__ == "__main__":
    words = ["alex","loves","leetcode"]
    print(Solution().shortestSuperstring(words))  # Output: "alexlovesleetcode"
