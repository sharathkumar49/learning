"""
1123. Lowest Common Ancestor of Deepest Leaves

Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

Constraints:
- The number of nodes in the tree is in the range [1, 1000].
- 0 <= Node.val <= 10^5

Example:
Input: root = [1,2,3]
Output: 1
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lcaDeepestLeaves(root: Optional[TreeNode]) -> Optional[TreeNode]:
    def dfs(node):
        if not node:
            return (0, None)
        l_depth, l_lca = dfs(node.left)
        r_depth, r_lca = dfs(node.right)
        if l_depth > r_depth:
            return (l_depth + 1, l_lca)
        if r_depth > l_depth:
            return (r_depth + 1, r_lca)
        return (l_depth + 1, node)
    return dfs(root)[1]

# Example usage:
from collections import deque

def build_tree(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = deque([root])
    i = 1
    while queue and i < len(lst):
        node = queue.popleft()
        if i < len(lst) and lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1
    return root

root = build_tree([1,2,3])
print(lcaDeepestLeaves(root).val)  # Output: 1
