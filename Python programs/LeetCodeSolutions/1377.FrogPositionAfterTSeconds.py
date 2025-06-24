"""
LeetCode 1377. Frog Position After T Seconds

Given a tree with n nodes and a frog starting at node 1, return the probability that the frog is on target after t seconds.

Constraints:
- 1 <= n <= 100
- edges.length == n-1
- 1 <= t <= 50
- 1 <= target <= n

Example:
Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4
Output: 0.16666666666666666
"""
def frogPosition(n, edges, t, target):
    from collections import defaultdict, deque
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    visited = [False]*(n+1)
    queue = deque([(1, 0, 1.0)])
    while queue:
        node, time, prob = queue.popleft()
        visited[node] = True
        if time == t or (node == target and (len(tree[node]) == 1 or node == 1)):
            if node == target:
                return prob
            continue
        cnt = sum(not visited[nei] for nei in tree[node])
        for nei in tree[node]:
            if not visited[nei]:
                queue.append((nei, time+1, prob/cnt))
    return 0.0

# Example usage:
n = 7
edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
t = 2
target = 4
print(frogPosition(n, edges, t, target))  # Output: 0.16666666666666666
