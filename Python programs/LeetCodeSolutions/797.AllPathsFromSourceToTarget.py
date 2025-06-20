"""
797. All Paths From Source to Target

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order. The graph is given as a list of lists, where graph[i] is a list of all nodes you can visit from node i.

Example 1:
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]

Example 2:
Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]

Constraints:
- n == graph.length
- 2 <= n <= 15
- 0 <= graph[i][j] < n
- graph[i] is sorted in a strictly increasing order.
- The graph is guaranteed to be a DAG.
"""
def allPathsSourceTarget(graph):
    res = []
    def dfs(path, node):
        if node == len(graph) - 1:
            res.append(path[:])
            return
        for nei in graph[node]:
            dfs(path + [nei], nei)
    dfs([0], 0)
    return res

# Example usage:
print(allPathsSourceTarget([[1,2],[3],[3],[]]))  # Output: [[0,1,3],[0,2,3]]
print(allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))  # Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
