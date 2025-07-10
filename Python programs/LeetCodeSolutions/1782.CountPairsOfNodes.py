"""
LeetCode 1782. Count Pairs Of Nodes

Given n nodes and a list of edges, and a list of queries, for each query return the number of pairs of nodes with a sum of degrees greater than the query value.

Example 1:
Input: n = 4, edges = [[1,2],[2,4],[1,3],[2,3],[2,1]], queries = [2,3]
Output: [6,5]

Constraints:
- 2 <= n <= 2 * 10^4
- 1 <= edges.length <= 10^5
- 1 <= queries.length <= 20
"""

def countPairs(n, edges, queries):
    from collections import Counter, defaultdict
    deg = [0]*(n+1)
    cnt = Counter()
    for u, v in edges:
        deg[u] += 1
        deg[v] += 1
        if u > v:
            u, v = v, u
        cnt[(u, v)] += 1
    res = []
    sorted_deg = sorted(deg[1:])
    for q in queries:
        ans = 0
        l, r = 0, n-1
        while l < r:
            if sorted_deg[l] + sorted_deg[r] > q:
                ans += r - l
                r -= 1
            else:
                l += 1
        for (u, v), c in cnt.items():
            if deg[u] + deg[v] > q and deg[u] + deg[v] - c <= q:
                ans -= 1
        res.append(ans)
    return res

# Example usage:
# n = 4
# edges = [[1,2],[2,4],[1,3],[2,3],[2,1]]
# queries = [2,3]
# print(countPairs(n, edges, queries))  # Output: [6,5]
