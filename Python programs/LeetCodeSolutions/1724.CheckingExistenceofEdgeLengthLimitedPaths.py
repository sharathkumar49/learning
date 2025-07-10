"""
LeetCode 1724. Checking Existence of Edge Length Limited Paths

You are given an undirected weighted graph with n nodes, an edge list, and queries. For each query [p, q, limit], return true if there is a path from p to q where every edge's weight is less than limit.

Example 1:
Input: n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8]], queries = [[0,2,5],[0,2,2]]
Output: [true,false]

Constraints:
- 2 <= n <= 10^5
- 1 <= edgeList.length, queries.length <= 10^5
- 0 <= edgeList[i][0], edgeList[i][1], p, q < n
- 1 <= edgeList[i][2], limit <= 10^9
"""

def distanceLimitedPathsExist(n, edgeList, queries):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    edgeList.sort(key=lambda x: x[2])
    queries = sorted([(limit, p, q, i) for i, (p, q, limit) in enumerate(queries)])
    res = [False] * len(queries)
    j = 0
    for limit, p, q, idx in queries:
        while j < len(edgeList) and edgeList[j][2] < limit:
            u, v, _ = edgeList[j]
            parent[find(u)] = find(v)
            j += 1
        res[idx] = find(p) == find(q)
    return res

# Example usage:
# n = 3
# edgeList = [[0,1,2],[1,2,4],[2,0,8]]
# queries = [[0,2,5],[0,2,2]]
# print(distanceLimitedPathsExist(n, edgeList, queries))  # Output: [True, False]
