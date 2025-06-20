"""
886. Possible Bipartition

Given n people and a list of dislikes, return true if it is possible to split everyone into two groups such that no pair in dislikes is in the same group.

Example 1:
Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true

Example 2:
Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false

Constraints:
- 1 <= n <= 2000
- 0 <= dislikes.length <= 10^4
- dislikes[i].length == 2
- 1 <= dislikes[i][j] <= n
- dislikes[i][0] < dislikes[i][1]
- All the pairs are unique.
"""
def possibleBipartition(n, dislikes):
    from collections import defaultdict, deque
    graph = defaultdict(list)
    for u, v in dislikes:
        graph[u].append(v)
        graph[v].append(u)
    color = {}
    for node in range(1, n+1):
        if node not in color:
            queue = deque([node])
            color[node] = 0
            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if v in color:
                        if color[v] == color[u]:
                            return False
                    else:
                        color[v] = 1 - color[u]
                        queue.append(v)
    return True

# Example usage:
print(possibleBipartition(4, [[1,2],[1,3],[2,4]]))  # Output: True
print(possibleBipartition(3, [[1,2],[1,3],[2,3]]))  # Output: False
