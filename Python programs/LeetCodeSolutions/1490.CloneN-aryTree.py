"""
LeetCode 1490. Clone N-ary Tree

Given a root of an N-ary tree, return a deep copy (clone) of the tree.

Constraints:
- The number of nodes in the tree is in the range [0, 1000].
- Each node's value is between [0, 10^4].

Example:
Input: root = [1,null,3,2,4,null,5,6]
Output: Deep copy of the tree
"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

def cloneTree(root):
    if not root:
        return None
    new_root = Node(root.val)
    new_root.children = [cloneTree(child) for child in root.children]
    return new_root

# Example usage:
# root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
# new_root = cloneTree(root)
