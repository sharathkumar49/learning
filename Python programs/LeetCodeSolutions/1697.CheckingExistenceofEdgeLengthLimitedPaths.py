"""
LeetCode 1697. Checking Existence of Edge Length Limited Paths

You are given an undirected weighted graph with n nodes, numbered from 0 to n - 1. You are also given an edge list and queries. For each query, check if there is a path between two nodes such that all edges on the path have weights strictly less than a given limit.

Example 1:
Input: n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8]], queries = [[0,2,5],[0,2,1],[0,1,3]]
Output: [true,false,true]

Constraints:
- 2 <= n <= 10^5
- 1 <= edgeList.length, queries.length <= 10^5
- 0 <= u, v, p, q < n
- 1 <= limit, edgeList[i][2] <= 10^9
"""

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

def distanceLimitedPathsExist(n, edgeList, queries):
    uf = UnionFind(n)
    edgeList.sort(key=lambda x: x[2])
    queries = [(p, q, limit, i) for i, (p, q, limit) in enumerate(queries)]
    queries.sort(key=lambda x: x[2])
    res = [False] * len(queries)
    j = 0
    for p, q, limit, idx in queries:
        while j < len(edgeList) and edgeList[j][2] < limit:
            uf.union(edgeList[j][0], edgeList[j][1])
            j += 1
        res[idx] = uf.find(p) == uf.find(q)
    return res

# Example usage:
# n = 3
# edgeList = [[0,1,2],[1,2,4],[2,0,8]]
# queries = [[0,2,5],[0,2,1],[0,1,3]]
# print(distanceLimitedPathsExist(n, edgeList, queries))  # Output: [True, False, True]
