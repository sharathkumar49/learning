"""
LeetCode 1791. Find Center of Star Graph

Given a star graph, return the center node.

Example 1:
Input: edges = [[1,2],[2,3],[4,2]]
Output: 2

Constraints:
- 3 <= n <= 10^5
- edges.length == n - 1
- edges[i].length == 2
- 1 <= edges[i][j] <= n
"""

def findCenter(edges):
    return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]

# Example usage:
# edges = [[1,2],[2,3],[4,2]]
# print(findCenter(edges))  # Output: 2
