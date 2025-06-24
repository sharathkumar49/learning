"""
1129. Shortest Path with Alternating Colors

Given a graph with n nodes and edges of red and blue colors, return the length of the shortest path from node 0 to every other node such that the path alternates colors.

Constraints:
- 1 <= n <= 100
- 0 <= red_edges.length, blue_edges.length <= 400
- red_edges[i].length == blue_edges[i].length == 2

Example:
Input: n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
Output: [0,1,-1]
"""
from typing import List
from collections import deque, defaultdict

def shortestAlternatingPaths(n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
    graph = [defaultdict(list) for _ in range(2)]  # 0: red, 1: blue
    for u, v in red_edges:
        graph[0][u].append(v)
    for u, v in blue_edges:
        graph[1][u].append(v)
    res = [-1] * n
    queue = deque([(0, 0, 0), (0, 1, 0)])  # node, color, length
    visited = set()
    while queue:
        node, color, length = queue.popleft()
        if res[node] == -1:
            res[node] = length
        visited.add((node, color))
        for nei in graph[1 - color][node]:
            if (nei, 1 - color) not in visited:
                queue.append((nei, 1 - color, length + 1))
    return res

# Example usage:
n = 3
red_edges = [[0,1],[1,2]]
blue_edges = []
print(shortestAlternatingPaths(n, red_edges, blue_edges))  # Output: [0, 1, -1]
