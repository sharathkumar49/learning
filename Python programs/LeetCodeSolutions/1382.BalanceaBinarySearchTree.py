"""
LeetCode 1382. Balance a Binary Search Tree

Given the root of a binary search tree, return a balanced binary search tree with the same node values.
A balanced binary search tree is a binary search tree in which the depth of the two subtrees of every node never differs by more than 1.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- 1 <= Node.val <= 10^5

Example:
Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def balanceBST(root):
    def inorder(node):
        return inorder(node.left) + [node] + inorder(node.right) if node else []
    nodes = inorder(root)
    def build(l, r):
        if l > r:
            return None
        m = (l + r) // 2
        node = nodes[m]
        node.left = build(l, m-1)
        node.right = build(m+1, r)
        return node
    return build(0, len(nodes)-1)

# Example usage:
# Build a BST and call balanceBST(root) as needed.
