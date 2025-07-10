"""
LeetCode 1617. Count Subtrees With Max Distance Between Cities

Given n cities and a list of edges, return an array answer where answer[i] is the number of subtrees with diameter i+1.

Example 1:
Input: n = 4, edges = [[1,2],[2,3],[2,4]]
Output: [3,4,0]

Constraints:
- 2 <= n <= 15
- edges.length == n-1
"""

def countSubgraphsForEachDiameter(n, edges):
    from collections import deque
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u-1].append(v-1)
        g[v-1].append(u-1)
    res = [0]*(n-1)
    for mask in range(1, 1<<n):
        nodes = [i for i in range(n) if mask & (1<<i)]
        if len(nodes) < 2:
            continue
        q = deque([nodes[0]])
        seen = {nodes[0]}
        parent = {nodes[0]: -1}
        while q:
            u = q.popleft()
            for v in g[u]:
                if v in nodes and v not in seen:
                    seen.add(v)
                    parent[v] = u
                    q.append(v)
        if len(seen) != len(nodes):
            continue
        def bfs(x):
            q = deque([(x, 0)])
            seen = {x}
            far, dist = x, 0
            while q:
                u, d = q.popleft()
                if d > dist:
                    far, dist = u, d
                for v in g[u]:
                    if v in nodes and v not in seen:
                        seen.add(v)
                        q.append((v, d+1))
            return far, dist
        _, d = bfs(nodes[0])
        _, d = bfs(_)
        if d > 0:
            res[d-1] += 1
    return res

# Example usage:
# n = 4
# edges = [[1,2],[2,3],[2,4]]
# print(countSubgraphsForEachDiameter(n, edges))  # Output: [3,4,0]
