"""
882. Reachable Nodes In Subdivided Graph

You are given an undirected graph (with some edges subdivided into more nodes). Return the number of nodes reachable from node 0 within maxMoves moves.

Example 1:
Input: edges = [[0,1,10],[0,2,1],[1,2,2]], maxMoves = 6, n = 3
Output: 13

Example 2:
Input: edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], maxMoves = 10, n = 4
Output: 23

Constraints:
- 0 <= edges.length <= min(n * (n - 1) / 2, 10^4)
- edges[i].length == 3
- 0 <= edges[i][0] < n
- 0 <= edges[i][1] < n
- 1 <= edges[i][2] <= 10^4
- 0 <= maxMoves <= 10^9
- 1 <= n <= 3000
"""
def reachableNodes(edges, maxMoves, n):
    import heapq
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    heap = [(-maxMoves, 0)]
    seen = {}
    while heap:
        moves, u = heapq.heappop(heap)
        moves = -moves
        if u in seen:
            continue
        seen[u] = moves
        for v, w in graph[u]:
            left = moves - w - 1
            if v not in seen and left >= 0:
                heapq.heappush(heap, (-left, v))
    res = len(seen)
    for u, v, w in edges:
        res += min(w, seen.get(u, 0) + seen.get(v, 0))
    return res

# Example usage:
print(reachableNodes([[0,1,10],[0,2,1],[1,2,2]], 6, 3))  # Output: 13
print(reachableNodes([[0,1,4],[1,2,6],[0,2,8],[1,3,1]], 10, 4))  # Output: 23
