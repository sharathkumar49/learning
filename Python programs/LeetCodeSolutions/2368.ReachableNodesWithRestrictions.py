"""
LeetCode 2368. Reachable Nodes With Restrictions

Given n, edges, and restricted, return the number of reachable nodes from node 0.

Example:
Input: n = 7, edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], restricted = [4,5]
Output: 4

Constraints:
- 2 <= n <= 10^5
"""

def reachableNodes(n, edges, restricted):
    from collections import defaultdict, deque
    g = defaultdict(list)
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    restricted = set(restricted)
    q = deque([0])
    seen = {0}
    res = 0
    while q:
        u = q.popleft()
        res += 1
        for v in g[u]:
            if v not in seen and v not in restricted:
                seen.add(v)
                q.append(v)
    return res

# Example usage:
# print(reachableNodes(7, [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], [4,5]))  # Output: 4
