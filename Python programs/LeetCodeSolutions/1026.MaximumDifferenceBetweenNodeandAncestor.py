"""
1026. Maximum Difference Between Node and Ancestor

Given the root of a binary tree, find the maximum value V for which there exists different nodes A and B such that V = |A.val - B.val| and A is an ancestor of B.

Constraints:
- The number of nodes in the tree is between 2 and 5000.
- 0 <= Node.val <= 10^5

Example:
Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: The maximum difference is between node 8 and node 1.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxAncestorDiff(root: Optional[TreeNode]) -> int:
    def dfs(node, mn, mx):
        if not node:
            return mx - mn
        mn = min(mn, node.val)
        mx = max(mx, node.val)
        return max(dfs(node.left, mn, mx), dfs(node.right, mn, mx))
    return dfs(root, root.val, root.val)

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

root = build_tree([8,3,10,1,6,None,14,None,None,4,7,13])
print(maxAncestorDiff(root))  # Output: 7
