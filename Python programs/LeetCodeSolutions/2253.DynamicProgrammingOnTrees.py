"""
LeetCode 2253. Dynamic Programming on Trees

Given a tree, return the minimum cost to cover all nodes.

Example:
Input: n = 3, edges = [[0,1],[1,2]], cost = [1,2,3]
Output: 3

Constraints:
- 1 <= n <= 10^5
"""

def minCostToCoverTree(n, edges, cost):
    from collections import defaultdict
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    dp = [0]*n
    def dfs(u, p):
        dp[u] = cost[u]
        for v in tree[u]:
            if v != p:
                dfs(v, u)
                dp[u] += min(dp[v], cost[v])
    dfs(0, -1)
    return min(dp)

# Example usage:
# print(minCostToCoverTree(3, [[0,1],[1,2]], [1,2,3]))  # Output: 3
