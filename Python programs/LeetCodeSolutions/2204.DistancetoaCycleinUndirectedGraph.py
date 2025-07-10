"""
LeetCode 2204. Distance to a Cycle in Undirected Graph

Given an undirected graph with vertices 1 to n, return an array answer of length n where answer[i] is the minimum distance from vertex i to any vertex involved in a cycle.

Example:
Input: n = 6, edges = [[1,4],[4,5],[2,3],[3,6],[5,6],[6,2]]
Output: [2,1,0,1,2,0]

Constraints:
- 3 <= n <= 10^5
- 2 <= edges.length <= min(10^5, n*(n-1)/2)
- edges[i].length == 2
- 1 <= ui, vi <= n
- ui != vi
"""

def distanceToCycle(n, edges):
    from collections import defaultdict, deque
    
    # Build graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    
    # Find cycle using DFS
    visited = set()
    parent = {}
    cycle = set()
    
    def dfs(node, par):
        visited.add(node)
        parent[node] = par
        for nei in graph[node]:
            if nei == par:
                continue
            if nei in visited:
                # Found cycle
                curr = node
                while curr != nei:
                    cycle.add(curr)
                    curr = parent[curr]
                cycle.add(nei)
                return True
            if dfs(nei, node):
                return True
        return False
    
    # Find any cycle
    for i in range(n):
        if i not in visited and dfs(i, -1):
            break
    
    # BFS to find distances
    answer = [0] * n
    q = deque([(i, 0) for i in cycle])
    seen = set(cycle)
    
    while q:
        node, dist = q.popleft()
        answer[node] = dist
        for nei in graph[node]:
            if nei not in seen:
                seen.add(nei)
                q.append((nei, dist + 1))
    
    return answer

# Example usage:
# print(distanceToCycle(6, [[1,4],[4,5],[2,3],[3,6],[5,6],[6,2]]))  # Output: [2,1,0,1,2,0]
