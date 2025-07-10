"""
LeetCode 1485. Clone Binary Tree With Random Pointer

Given a binary tree with a random pointer for each node, return a deep copy of the tree.

Constraints:
- The number of nodes in the tree is in the range [0, 1000].
- Each node's value is between [0, 10^6].

Example:
Input: root = [1,4,7,null,null,2,6], random = [[1,7],[2,4],[4,2],[6,1],[7,6]]
Output: Deep copy of the tree
"""
class Node:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random

def copyRandomBinaryTree(root):
    from collections import defaultdict
    old_to_new = defaultdict(lambda: None)
    def clone(node):
        if not node:
            return None
        if node in old_to_new:
            return old_to_new[node]
        new_node = Node(node.val)
        old_to_new[node] = new_node
        new_node.left = clone(node.left)
        new_node.right = clone(node.right)
        new_node.random = clone(node.random)
        return new_node
    return clone(root)

# Example usage:
# root = Node(1)
# ... (build tree and set random pointers)
# new_root = copyRandomBinaryTree(root)
