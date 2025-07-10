"""
LeetCode 1615. Maximal Network Rank

Given an infrastructure of n cities and a list of roads, return the maximal network rank of the infrastructure.

Example 1:
Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
Output: 4

Constraints:
- 2 <= n <= 100
- 0 <= roads.length <= n * (n - 1) / 2
- roads[i].length == 2
"""

def maximalNetworkRank(n, roads):
    deg = [0]*n
    conn = set()
    for a, b in roads:
        deg[a] += 1
        deg[b] += 1
        conn.add((a,b))
        conn.add((b,a))
    res = 0
    for i in range(n):
        for j in range(i+1, n):
            r = deg[i] + deg[j] - ((i,j) in conn)
            res = max(res, r)
    return res

# Example usage:
# n = 4
# roads = [[0,1],[0,3],[1,2],[1,3]]
# print(maximalNetworkRank(n, roads))  # Output: 4
