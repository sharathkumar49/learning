"""
LeetCode 1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree

Given a weighted undirected connected graph with n vertices and an array edges, return a list of critical and pseudo-critical edges in the MST.

Constraints:
- 2 <= n <= 100
- 1 <= edges.length <= min(200, n * (n - 1) / 2)
- edges[i].length == 3
- 0 <= from_i < to_i < n
- 1 <= weight_i <= 1000

Example:
Input: n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
Output: [[0,1],[2,3,4,5]]
"""
def findCriticalAndPseudoCriticalEdges(n, edges):
    from collections import defaultdict
    class DSU:
        def __init__(self, n):
            self.p = list(range(n))
        def find(self, x):
            if self.p[x] != x:
                self.p[x] = self.find(self.p[x])
            return self.p[x]
        def union(self, x, y):
            self.p[self.find(x)] = self.find(y)
    new_edges = [e + [i] for i, e in enumerate(edges)]
    new_edges.sort(key=lambda x: x[2])
    def kruskal(block=-1, force=-1):
        dsu = DSU(n)
        weight = 0
        cnt = 0
        if force != -1:
            u, v, w, _ = new_edges[force]
            dsu.union(u, v)
            weight += w
            cnt += 1
        for i, (u, v, w, idx) in enumerate(new_edges):
            if i == block:
                continue
            if dsu.find(u) != dsu.find(v):
                dsu.union(u, v)
                weight += w
                cnt += 1
        return weight if cnt == n-1 else float('inf')
    min_weight = kruskal()
    critical, pseudo = [], []
    for i in range(len(new_edges)):
        if kruskal(block=i) > min_weight:
            critical.append(new_edges[i][3])
        elif kruskal(force=i) == min_weight:
            pseudo.append(new_edges[i][3])
    return [critical, pseudo]

# Example usage:
n = 5
edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
print(findCriticalAndPseudoCriticalEdges(n, edges))  # Output: [[0,1],[2,3,4,5]]
