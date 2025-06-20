"""
314. Binary Tree Vertical Order Traversal

Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

Constraints:
- The number of nodes in the tree is in the range [0, 1000].
- -100 <= Node.val <= 100
"""
from typing import List, Optional
from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        col_table = defaultdict(list)
        queue = deque([(root, 0)])
        min_col = max_col = 0
        while queue:
            node, col = queue.popleft()
            if node:
                col_table[col].append(node.val)
                min_col = min(min_col, col)
                max_col = max(max_col, col)
                queue.append((node.left, col - 1))
                queue.append((node.right, col + 1))
        return [col_table[x] for x in range(min_col, max_col + 1)]

# Example usage:
# root = TreeNode(3, TreeNode(9), TreeNode(8, TreeNode(4), TreeNode(1)))
# print(Solution().verticalOrder(root))
