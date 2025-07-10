"""
LeetCode 1483. Kth Ancestor of a Tree Node

You are given a tree with n nodes numbered from 0 to n-1 in the form of a parent array. Implement the TreeAncestor class with a getKthAncestor(node, k) method that returns the k-th ancestor of the given node.

Constraints:
- 1 <= n <= 5 * 10^4
- 0 <= parent[i] < n
- parent[0] == -1
- 0 <= node < n
- 1 <= k <= n

Example:
Input: n = 7, parent = [-1,0,0,1,1,2,2], queries = [(3,1),(5,2),(6,3)]
Output: [1,0,-1]
"""
class TreeAncestor:
    def __init__(self, n, parent):
        LOG = 16
        self.up = [[-1]*LOG for _ in range(n)]
        for v in range(n):
            self.up[v][0] = parent[v]
        for j in range(1, LOG):
            for v in range(n):
                if self.up[v][j-1] != -1:
                    self.up[v][j] = self.up[self.up[v][j-1]][j-1]

    def getKthAncestor(self, node, k):
        for j in range(16):
            if k & (1 << j):
                node = self.up[node][j]
                if node == -1:
                    break
        return node

# Example usage:
# n = 7
# parent = [-1,0,0,1,1,2,2]
# tree = TreeAncestor(n, parent)
# print(tree.getKthAncestor(3, 1))  # Output: 1
# print(tree.getKthAncestor(5, 2))  # Output: 0
# print(tree.getKthAncestor(6, 3))  # Output: -1
