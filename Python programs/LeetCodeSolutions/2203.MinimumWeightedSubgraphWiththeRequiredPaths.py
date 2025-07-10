"""
LeetCode 2203. Minimum Weighted Subgraph With the Required Paths

Given a weighted directed graph with n vertices, find the minimum weight of a subgraph that contains paths from src1 to dest and from src2 to dest.

Example:
Input: n = 6, edges = [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,4,4],[3,4,2],[4,5,1]], src1 = 0, src2 = 1, dest = 5
Output: 9

Constraints:
- 3 <= n <= 10^5
- 0 <= edges.length <= 10^5
- edges[i].length == 3
- 0 <= fromi, toi < n
- fromi != toi
- 1 <= weighti <= 10^4
- 0 <= src1, src2, dest < n
- src1, src2, and dest are different.
"""

def minimumWeight(n, edges, src1, src2, dest):
    from collections import defaultdict
    import heapq
    
    def dijkstra(graph, start):
        dist = [float('inf')] * n
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
        return dist

    # Build forward and reverse graphs
    graph = defaultdict(list)
    rev_graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        rev_graph[v].append((u, w))

    # Find shortest paths
    dist1 = dijkstra(graph, src1)
    dist2 = dijkstra(graph, src2)
    dist3 = dijkstra(rev_graph, dest)

    # Find minimum total weight
    result = float('inf')
    for i in range(n):
        if dist1[i] != float('inf') and dist2[i] != float('inf') and dist3[i] != float('inf'):
            result = min(result, dist1[i] + dist2[i] + dist3[i])

    return result if result != float('inf') else -1

# Example usage:
# edges = [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,4,4],[3,4,2],[4,5,1]]
# print(minimumWeight(6, edges, 0, 1, 5))  # Output: 9
