"""
LeetCode 1931. Paint House III

Given an array houses, an integer m, an integer n, and an array cost, return the minimum cost to paint all houses such that there are exactly target neighborhoods.

Example:
Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
Output: 9

Constraints:
- m == houses.length
- n == cost[i].length
- 1 <= m <= 100
- 1 <= n <= 20
- 1 <= cost[i][j] <= 10^4
- 0 <= houses[i] <= n
- 1 <= target <= m
"""

def minCost(houses, cost, m, n, target):
    from functools import lru_cache
    INF = float('inf')
    @lru_cache(None)
    def dp(i, prev, t):
        if t < 0: return INF
        if i == m: return 0 if t == 0 else INF
        if houses[i]:
            return dp(i+1, houses[i], t-(houses[i]!=prev))
        return min(cost[i][j-1] + dp(i+1, j, t-(j!=prev)) for j in range(1, n+1))
    res = dp(0, 0, target)
    return res if res < INF else -1

# Example usage:
# print(minCost([0,0,0,0,0], [[1,10],[10,1],[10,1],[1,10],[5,1]], 5, 2, 3))  # Output: 9
