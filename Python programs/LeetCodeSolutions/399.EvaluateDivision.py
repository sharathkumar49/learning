"""
399. Evaluate Division

You are given equations in the format A / B = k, where A and B are variables and k is a real number. Given some queries, return the answers. If the answer does not exist, return -1.0.

Constraints:
- 1 <= equations.length <= 20
- equations[i].length == 2
- 1 <= values.length, queries.length <= 20
- values[i] is a real number between 0.0 and 20.0
- queries[i].length == 2
- 1 <= A, B, C, D <= 5
- A, B, C, D are lowercase English letters and represent single variables.
"""
from typing import List
from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (a, b), v in zip(equations, values):
            graph[a][b] = v
            graph[b][a] = 1 / v
        def bfs(src, dst):
            if src not in graph or dst not in graph:
                return -1.0
            queue = deque([(src, 1.0)])
            visited = set()
            while queue:
                node, prod = queue.popleft()
                if node == dst:
                    return prod
                visited.add(node)
                for nei, val in graph[node].items():
                    if nei not in visited:
                        queue.append((nei, prod * val))
            return -1.0
        return [bfs(a, b) for a, b in queries]

# Example usage:
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
print(Solution().calcEquation(equations, values, queries))  # Output: [6.0,0.5,-1.0,1.0,-1.0]
