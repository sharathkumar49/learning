"""
LeetCode 687. Longest Univalue Path

Given the root of a binary tree, return the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.
The length of the path between two nodes is represented by the number of edges between them.

Example 1:
Input: root = [5,4,5,1,1,5]
Output: 2

Example 2:
Input: root = [1,4,5,4,4,5]
Output: 2

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- -1000 <= Node.val <= 1000
- The depth of the tree will not exceed 1000.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def longestUnivaluePath(root: Optional[TreeNode]) -> int:
    res = 0
    def dfs(node):
        nonlocal res
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        left_path = right_path = 0
        if node.left and node.left.val == node.val:
            left_path = left + 1
        if node.right and node.right.val == node.val:
            right_path = right + 1
        res = max(res, left_path + right_path)
        return max(left_path, right_path)
    dfs(root)
    return res

# Example usage
if __name__ == "__main__":
    # Helper to build tree for testing
    def build_tree(vals):
        nodes = [TreeNode(v) if v is not None else None for v in vals]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root
    root = build_tree([5,4,5,1,1,None,5])
    print(longestUnivaluePath(root))  # Output: 2
    root = build_tree([1,4,5,4,4,None,5])
    print(longestUnivaluePath(root))  # Output: 2
