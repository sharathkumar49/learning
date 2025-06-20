"""
785. Is Graph Bipartite?

Given an undirected graph, return true if and only if it is bipartite.
The graph is given as an adjacency list, where graph[i] is a list of nodes that node i is connected to.

Example 1:
Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false

Example 2:
Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true

Constraints:
- 1 <= graph.length <= 100
- 0 <= graph[i].length < graph.length
- 0 <= graph[i][j] < graph.length
"""
def isBipartite(graph):
    color = {}
    for node in range(len(graph)):
        if node not in color:
            stack = [node]
            color[node] = 0
            while stack:
                u = stack.pop()
                for v in graph[u]:
                    if v in color:
                        if color[v] == color[u]:
                            return False
                    else:
                        color[v] = 1 - color[u]
                        stack.append(v)
    return True

# Example usage:
print(isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))  # Output: False
print(isBipartite([[1,3],[0,2],[1,3],[0,2]]))      # Output: True
