"""
LeetCode 1971. Find if Path Exists in Graph

Given n nodes and a list of edges, return true if there is a valid path between start and end.

Example:
Input: n = 3, edges = [[0,1],[1,2],[2,0]], start = 0, end = 2
Output: true

Constraints:
- 1 <= n <= 2 * 10^5
- 0 <= edges.length <= 2 * 10^5
- 0 <= start, end < n
"""

def validPath(n, edges, start, end):
    from collections import defaultdict, deque
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    q = deque([start])
    seen = set([start])
    while q:
        node = q.popleft()
        if node == end:
            return True
        for nei in graph[node]:
            if nei not in seen:
                seen.add(nei)
                q.append(nei)
    return False

# Example usage:
# print(validPath(3, [[0,1],[1,2],[2,0]], 0, 2))  # Output: True
