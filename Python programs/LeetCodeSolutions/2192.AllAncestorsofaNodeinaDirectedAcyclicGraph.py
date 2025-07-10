"""
LeetCode 2192. All Ancestors of a Node in a Directed Acyclic Graph

Given a DAG of n nodes labeled from 0 to n-1, and a list of edges, return a list of lists where the i-th list contains all ancestors of node i in sorted order.

Example:
Input: n = 8, edges = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
Output: [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]

Constraints:
- 1 <= n <= 1000
- edges.length <= min(2000, n*(n-1)/2)
"""

def getAncestors(n, edges):
    from collections import defaultdict, deque
    graph = defaultdict(list)
    indegree = [0]*n
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1
    ancestors = [set() for _ in range(n)]
    q = deque([i for i in range(n) if indegree[i]==0])
    while q:
        u = q.popleft()
        for v in graph[u]:
            ancestors[v] |= ancestors[u]
            ancestors[v].add(u)
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
    return [sorted(list(a)) for a in ancestors]

# Example usage:
# print(getAncestors(8, [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]))
