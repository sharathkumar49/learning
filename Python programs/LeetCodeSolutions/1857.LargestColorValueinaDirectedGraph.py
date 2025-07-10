"""
LeetCode 1857. Largest Color Value in a Directed Graph

You are given a directed graph of n colored nodes, where the color of the i-th node is colors[i] and edges[i] = [ai, bi] indicates a directed edge from ai to bi. Return the largest color value in any valid path. If there is a cycle, return -1.

Example 1:
Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
Output: 3

Constraints:
- 1 <= n <= 10^5
- colors.length == n
- 0 <= edges.length <= min(n * (n - 1) / 2, 10^5)
"""

def largestPathValue(colors, edges):
    from collections import defaultdict, deque
    n = len(colors)
    graph = defaultdict(list)
    indegree = [0]*n
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1
    count = [ [0]*26 for _ in range(n)]
    q = deque([i for i in range(n) if indegree[i]==0])
    res = 0
    seen = 0
    while q:
        u = q.popleft()
        seen += 1
        c = ord(colors[u])-ord('a')
        count[u][c] += 1
        res = max(res, count[u][c])
        for v in graph[u]:
            for i in range(26):
                count[v][i] = max(count[v][i], count[u][i])
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
    return res if seen == n else -1

# Example usage:
# colors = "abaca"
# edges = [[0,1],[0,2],[2,3],[3,4]]
# print(largestPathValue(colors, edges))  # Output: 3
