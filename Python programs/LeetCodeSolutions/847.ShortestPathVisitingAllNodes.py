"""
847. Shortest Path Visiting All Nodes

Given an undirected, connected graph of n nodes, return the length of the shortest path that visits every node. You may start and stop at any node, revisit nodes multiple times, and reuse edges.

Example 1:
Input: graph = [[1,2,3],[0],[0],[0]]
Output: 4

Example 2:
Input: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
Output: 4

Constraints:
- n == graph.length
- 1 <= n <= 12
- 0 <= graph[i].length < n
- 0 <= graph[i][j] < n
- All the edges are undirected and the graph is connected.
"""
def shortestPathLength(graph):
    from collections import deque
    n = len(graph)
    queue = deque((i, 1 << i, 0) for i in range(n))
    seen = {(i, 1 << i) for i in range(n)}
    while queue:
        node, mask, dist = queue.popleft()
        if mask == (1 << n) - 1:
            return dist
        for nei in graph[node]:
            next_mask = mask | (1 << nei)
            if (nei, next_mask) not in seen:
                seen.add((nei, next_mask))
                queue.append((nei, next_mask, dist + 1))
    return -1

# Example usage:
print(shortestPathLength([[1,2,3],[0],[0],[0]]))  # Output: 4
print(shortestPathLength([[1],[0,2,4],[1,3,4],[2],[1,2]]))  # Output: 4
