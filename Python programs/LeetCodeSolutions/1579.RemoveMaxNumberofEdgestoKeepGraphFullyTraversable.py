"""
LeetCode 1579. Remove Max Number of Edges to Keep Graph Fully Traversable

Alice and Bob have an undirected graph of n nodes and three types of edges:
- Type 1: Can be traversed by Alice only.
- Type 2: Can be traversed by Bob only.
- Type 3: Can be traversed by both Alice and Bob.

Given an array edges where edges[i] = [type, u, v] represents a type of edge between nodes u and v, return the maximum number of edges you can remove so that the graph is still fully traversable by both Alice and Bob. If the graph cannot be fully traversed by both, return -1.

Example 1:
Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
Output: 2

Example 2:
Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
Output: 0

Constraints:
- 1 <= n <= 10^5
- 1 <= edges.length <= min(10^5, 3 * n * (n - 1) / 2)
- edges[i].length == 3
- 1 <= type <= 3
- 1 <= u < v <= n
- All pairs (type, u, v) are distinct.
"""

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
        self.sets = n
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        if self.rank[xr] < self.rank[yr]:
            self.parent[xr] = yr
        else:
            self.parent[yr] = xr
            if self.rank[xr] == self.rank[yr]:
                self.rank[xr] += 1
        self.sets -= 1
        return True

def maxNumEdgesToRemove(n, edges):
    alice = DSU(n)
    bob = DSU(n)
    res = 0
    for t,u,v in edges:
        if t == 3:
            if not (alice.union(u-1,v-1) | bob.union(u-1,v-1)):
                res += 1
    for t,u,v in edges:
        if t == 1:
            if not alice.union(u-1,v-1):
                res += 1
        elif t == 2:
            if not bob.union(u-1,v-1):
                res += 1
    if alice.sets > 1 or bob.sets > 1:
        return -1
    return res

# Example usage:
# n = 4
# edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
# print(maxNumEdgesToRemove(n, edges))  # Output: 2
