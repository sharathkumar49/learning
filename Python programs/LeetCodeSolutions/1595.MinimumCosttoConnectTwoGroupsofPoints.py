"""
LeetCode 1595. Minimum Cost to Connect Two Groups of Points

Given two groups of points, cost[i][j] is the cost of connecting point i in group 1 to point j in group 2. Return the minimum cost to connect each point in both groups to at least one point in the other group.

Example 1:
Input: cost = [[15,96],[36,2]]
Output: 17

Constraints:
- 1 <= cost.length, cost[0].length <= 12
- 1 <= cost[i][j] <= 100
"""

def connectTwoGroups(cost):
    from functools import lru_cache
    m, n = len(cost), len(cost[0])
    @lru_cache(None)
    def dp(i, mask):
        if i == m:
            res = 0
            for j in range(n):
                if not (mask & (1<<j)):
                    res += min(cost[k][j] for k in range(m))
            return res
        res = float('inf')
        for j in range(n):
            res = min(res, cost[i][j] + dp(i+1, mask | (1<<j)))
        return res
    return dp(0, 0)

# Example usage:
# cost = [[15,96],[36,2]]
# print(connectTwoGroups(cost))  # Output: 17
