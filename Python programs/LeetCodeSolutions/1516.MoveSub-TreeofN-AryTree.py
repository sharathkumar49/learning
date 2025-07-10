"""
LeetCode 1516. Move Sub-Tree of N-Ary Tree

Given the root of an N-ary tree and two nodes p and q, move the subtree of p to become a child of q.

Constraints:
- The number of nodes in the tree is in the range [1, 1000].
- Each node's value is between [0, 10^4].

Example:
Input: root = [1,null,2,3,4,5,null,null,6], p = 3, q = 4
Output: Modified tree
"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

def moveSubTree(root, p, q):
    def findParent(node, target, parent=None):
        if not node:
            return None
        if node == target:
            return parent
        for child in node.children:
            res = findParent(child, target, node)
            if res:
                return res
        return None
    parent_p = findParent(root, p)
    if parent_p:
        parent_p.children.remove(p)
    q.children.append(p)
    return root

# Example usage:
# root = Node(1, [Node(2), Node(3), Node(4), Node(5)])
# p = root.children[1]
# q = root.children[2]
# moveSubTree(root, p, q)
