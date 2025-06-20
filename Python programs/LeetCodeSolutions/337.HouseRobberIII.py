"""
337. House Robber III

The thief has found himself a new place for his thievery again. There is only one entrance to this house, which consists of a binary tree. Each node in the tree represents a house with a certain amount of money. If two directly-linked houses are robbed on the same night, the house will automatically contact the police.

Return the maximum amount of money the thief can rob tonight without alerting the police.

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- 0 <= Node.val <= 10^4
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return (0, 0)
            left = helper(node.left)
            right = helper(node.right)
            rob = node.val + left[1] + right[1]
            not_rob = max(left) + max(right)
            return (rob, not_rob)
        return max(helper(root))

# Example usage:
# root = TreeNode(3, TreeNode(2, None, TreeNode(3)), TreeNode(3, None, TreeNode(1)))
# print(Solution().rob(root))  # Output: 7
