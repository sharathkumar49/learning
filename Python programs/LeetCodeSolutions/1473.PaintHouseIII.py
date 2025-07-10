"""
LeetCode 1473. Paint House III

Given an array houses, an m x n matrix cost, and an integer target, return the minimum cost of painting the houses such that there are exactly target neighborhoods. If it is not possible, return -1.

Constraints:
- 1 <= m <= 100
- 1 <= n <= 20
- 1 <= target <= m
- 0 <= houses[i] <= n
- 1 <= cost[i][j] <= 10^4

Example:
Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
Output: 9
"""
def minCost(houses, cost, m, n, target):
    from functools import lru_cache
    INF = float('inf')
    @lru_cache(None)
    def dp(i, prev_color, t):
        if t < 0:
            return INF
        if i == m:
            return 0 if t == 0 else INF
        if houses[i]:
            return dp(i+1, houses[i], t-(houses[i]!=prev_color))
        res = INF
        for color in range(1, n+1):
            res = min(res, cost[i][color-1] + dp(i+1, color, t-(color!=prev_color)))
        return res
    ans = dp(0, 0, target)
    return -1 if ans == INF else ans

# Example usage:
houses = [0,0,0,0,0]
cost = [[1,10],[10,1],[10,1],[1,10],[5,1]]
m, n, target = 5, 2, 3
print(minCost(houses, cost, m, n, target))  # Output: 9
