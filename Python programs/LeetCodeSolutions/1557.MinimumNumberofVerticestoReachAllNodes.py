"""
LeetCode 1557. Minimum Number of Vertices to Reach All Nodes

Given a directed acyclic graph, return the smallest set of vertices from which all nodes are reachable.

Constraints:
- 2 <= n <= 10^5
- 1 <= edges.length <= min(10^5, n * (n - 1) / 2)
- edges[i].length == 2
- 0 <= from_i, to_i < n

Example:
Input: n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
Output: [0,3]
"""
def findSmallestSetOfVertices(n, edges):
    to = set(j for i, j in edges)
    return [i for i in range(n) if i not in to]

# Example usage:
n = 6
edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
print(findSmallestSetOfVertices(n, edges))  # Output: [0, 3]
