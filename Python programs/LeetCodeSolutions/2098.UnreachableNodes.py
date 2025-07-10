"""
LeetCode 2098. Unreachable Nodes

Given n nodes and a list of edges, return the number of unreachable pairs of nodes.

Example:
Input: n = 3, edges = [[0,1],[0,2]]
Output: 0

Constraints:
- 1 <= n <= 10^5
- 0 <= edges.length <= 2 * 10^5
"""

def countPairs(n, edges):
    from collections import defaultdict, deque
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited = [False] * n
    sizes = []
    for i in range(n):
        if not visited[i]:
            q = deque([i])
            visited[i] = True
            size = 1
            while q:
                u = q.popleft()
                for v in graph[u]:
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)
                        size += 1
            sizes.append(size)
    total = n * (n - 1) // 2
    for s in sizes:
        total -= s * (s - 1) // 2
    return total

# Example usage:
# print(countPairs(3, [[0,1],[0,2]]))  # Output: 0
