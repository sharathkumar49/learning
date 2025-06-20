"""
589. N-ary Tree Preorder Traversal
Difficulty: Easy

Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]

Constraints:
The number of nodes in the tree is in the range [0, 10^4].
The height of the n-ary tree is less than or equal to 1000.
"""

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

def preorder(root: 'Node'):
    res = []
    def dfs(node):
        if not node:
            return
        res.append(node.val)
        for child in node.children:
            dfs(child)
    dfs(root)
    return res

# Example usage
# (See LeetCode for N-ary tree construction examples)
