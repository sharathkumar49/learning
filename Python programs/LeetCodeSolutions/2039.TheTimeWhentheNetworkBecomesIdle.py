"""
LeetCode 2039. The Time When the Network Becomes Idle

Given a network, return the earliest second when the network becomes idle.

Example:
Input: edges = [[0,1],[1,2]], patience = [0,2,1]
Output: 8

Constraints:
- n == patience.length
- 2 <= n <= 10^5
- patience[i] in [0, 10^9]
"""

def networkBecomesIdle(edges, patience):
    from collections import deque, defaultdict
    n = len(patience)
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    # BFS to find shortest path from node 0
    dist = [float('inf')] * n
    dist[0] = 0
    q = deque([0])
    while q:
        u = q.popleft()
        for v in graph[u]:
            if dist[v] == float('inf'):
                dist[v] = dist[u] + 1
                q.append(v)
    res = 0
    for i in range(1, n):
        d = dist[i] * 2
        if patience[i] >= d:
            last = d
        else:
            last = ((d - 1) // patience[i]) * patience[i] + d
        res = max(res, last)
    return res + 1

# Example usage:
# print(networkBecomesIdle([[0,1],[1,2]], [0,2,1]))  # Output: 8
