"""
1245. Tree Diameter

Given an undirected tree, return its diameter (the length of the longest path between any two nodes).

Constraints:
- 2 <= edges.length <= 10^4
- edges[i].length == 2
- 0 <= edges[i][j] < edges.length + 1

Example:
Input: edges = [[0,1],[1,2],[1,3],[3,4],[4,5]]
Output: 4

"""
def treeDiameter(edges):
    from collections import defaultdict, deque
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    def bfs(start):
        visited = set([start])
        q = deque([(start, 0)])
        farthest, dist = start, 0
        while q:
            node, d = q.popleft()
            if d > dist:
                farthest, dist = node, d
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append((nei, d+1))
        return farthest, dist
    far, _ = bfs(0)
    _, diameter = bfs(far)
    return diameter

# Example usage
if __name__ == "__main__":
    edges = [[0,1],[1,2],[1,3],[3,4],[4,5]]
    print(treeDiameter(edges))  # Output: 4
