"""
LeetCode 1900. The Earliest and Latest Rounds Where Players Compete

Given n players, and two players a and b, return the earliest and latest rounds in which they can compete.

Example:
Input: n = 11, a = 2, b = 4
Output: [3,4]

Constraints:
- 2 <= n <= 28
- 1 <= a < b <= n
"""

def earliestAndLatest(n, a, b):
    from functools import lru_cache
    @lru_cache(None)
    def dfs(players, r):
        if a in players and b in players:
            i, j = players.index(a), players.index(b)
            if i + j == len(players) - 1:
                return (r, r)
        if len(players) == 1:
            return (float('inf'), -float('inf'))
        res = (float('inf'), -float('inf'))
        m = len(players)
        for mask in range(1 << (m // 2)):
            nxt = []
            for i in range(m // 2):
                if mask & (1 << i):
                    nxt.append(players[m - 1 - i])
                else:
                    nxt.append(players[i])
            if m % 2:
                nxt.append(players[m // 2])
            t = dfs(tuple(nxt), r + 1)
            res = (min(res[0], t[0]), max(res[1], t[1]))
        return res
    return list(dfs(tuple(range(1, n+1)), 1))

# Example usage:
# print(earliestAndLatest(11, 2, 4))  # Output: [3, 4]
