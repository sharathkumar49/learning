"""
LeetCode 2196. Create Binary Tree From Descriptions

Given a list of descriptions, where each description is [parent, child, isLeft], build the binary tree and return its root.

Example:
Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
Output: [50,20,80,15,17,19]

Constraints:
- 1 <= descriptions.length <= 10^4
- 1 <= parent, child <= 10^5
- 0 <= isLeft <= 1
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createBinaryTree(descriptions):
    nodes = {}
    child_set = set()
    for p, c, isLeft in descriptions:
        if p not in nodes:
            nodes[p] = TreeNode(p)
        if c not in nodes:
            nodes[c] = TreeNode(c)
        if isLeft:
            nodes[p].left = nodes[c]
        else:
            nodes[p].right = nodes[c]
        child_set.add(c)
    root = (set(nodes) - child_set).pop()
    return nodes[root]

# Example usage:
# (You would need to traverse the tree to print the result)
