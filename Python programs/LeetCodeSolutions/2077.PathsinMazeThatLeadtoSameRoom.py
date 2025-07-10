"""
LeetCode 2077. Paths in Maze That Lead to Same Room

Given a maze, return the number of paths that lead to the same room.

Example:
Input: n = 4, corridors = [[0,1],[1,2],[1,3]]
Output: 1

Constraints:
- 2 <= n <= 10^5
- 1 <= corridors.length <= 10^5
"""

def numberOfPaths(n, corridors):
    from collections import defaultdict
    graph = defaultdict(list)
    for u, v in corridors:
        graph[u].append(v)
        graph[v].append(u)
    res = 0
    for u in range(n):
        for v in graph[u]:
            for w in graph[v]:
                if w != u and u in graph[w]:
                    res += 1
    return res // 6

# Example usage:
# print(numberOfPaths(4, [[0,1],[1,2],[1,3]]))  # Output: 1
