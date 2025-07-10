"""
LeetCode 1469. Find All The Lonely Nodes

Given the root of a binary tree, return an array containing the values of all lonely nodes in the tree. A lonely node is a node that is the only child of its parent.

Constraints:
- The number of nodes in the tree is in the range [1, 1000].
- 1 <= Node.val <= 10^6

Example:
Input: root = [1,2,3,null,4]
Output: [4]
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getLonelyNodes(root):
    res = []
    def dfs(node):
        if not node:
            return
        if node.left and not node.right:
            res.append(node.left.val)
        if node.right and not node.left:
            res.append(node.right.val)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return res

# Example usage:
# root = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3))
# print(getLonelyNodes(root))  # Output: [4]
