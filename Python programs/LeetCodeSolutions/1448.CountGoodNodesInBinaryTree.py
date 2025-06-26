"""
LeetCode 1448. Count Good Nodes in Binary Tree

Given a binary tree, return the number of good nodes. A node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Constraints:
- The number of nodes in the binary tree is in the range [1, 10^5].
- -10^4 <= Node.val <= 10^4

Example:
Input: root = [3,1,4,3,null,1,5]
Output: 4
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def goodNodes(root):
    def dfs(node, max_val):
        if not node:
            return 0
        res = 1 if node.val >= max_val else 0
        max_val = max(max_val, node.val)
        res += dfs(node.left, max_val)
        res += dfs(node.right, max_val)
        return res
    return dfs(root, root.val)

# Example usage:
# Tree: 3,1,4,3,null,1,5
root = TreeNode(3,
    TreeNode(1, TreeNode(3)),
    TreeNode(4, TreeNode(1), TreeNode(5))
)
print(goodNodes(root))  # Output: 4
