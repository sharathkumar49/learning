"""
510. Inorder Successor in BST II

Given a node in a binary search tree, return its in-order successor. Each node has a parent pointer. If the node has no in-order successor, return null.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -10^5 <= Node.val <= 10^5

Example:
Input: node = 2 (in BST: [2,1,3])
Output: 3
"""

class Node:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        while node.parent and node == node.parent.right:
            node = node.parent
        return node.parent

# Example usage:
# Not executable without a full BST with parent pointers.
