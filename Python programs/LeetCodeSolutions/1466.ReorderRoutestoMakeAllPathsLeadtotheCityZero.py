"""
LeetCode 1466. Reorder Routes to Make All Paths Lead to the City Zero

There are n cities numbered from 0 to n-1 and n-1 roads. Each road is represented as a pair [a, b] indicating a road from city a to city b. Return the minimum number of edges you must reverse so that every city can reach city 0.

Constraints:
- 2 <= n <= 5 * 10^4
- roads.length == n - 1
- roads[i].length == 2
- 0 <= a, b < n

Example:
Input: n = 6, roads = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
"""
def minReorder(n, connections):
    from collections import defaultdict, deque
    graph = defaultdict(list)
    for a, b in connections:
        graph[a].append((b, 1))
        graph[b].append((a, 0))
    res = 0
    visited = set()
    q = deque([0])
    while q:
        node = q.popleft()
        visited.add(node)
        for nei, cost in graph[node]:
            if nei not in visited:
                res += cost
                q.append(nei)
    return res

# Example usage:
n = 6
roads = [[0,1],[1,3],[2,3],[4,0],[4,5]]
print(minReorder(n, roads))  # Output: 3
