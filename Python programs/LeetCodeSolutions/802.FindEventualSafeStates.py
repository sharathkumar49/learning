"""
802. Find Eventual Safe States

Given a directed graph, return a list of all the nodes that are eventually safe. The graph is given as a list of lists, where graph[i] is a list of nodes you can visit from node i.

Example 1:
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]

Example 2:
Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
Output: [4]

Constraints:
- n == graph.length
- 1 <= n <= 10^4
- 0 <= graph[i].length <= n
- 0 <= graph[i][j] < n
"""
def eventualSafeNodes(graph):
    n = len(graph)
    color = [0] * n
    def dfs(node):
        if color[node] > 0:
            return color[node] == 2
        color[node] = 1
        for nei in graph[node]:
            if not dfs(nei):
                return False
        color[node] = 2
        return True
    return [i for i in range(n) if dfs(i)]

# Example usage:
print(eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))  # Output: [2,4,5,6]
print(eventualSafeNodes([[1,2,3,4],[1,2],[3,4],[0,4],[]]))  # Output: [4]
