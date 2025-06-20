"""
958. Check Completeness of a Binary Tree
https://leetcode.com/problems/check-completeness-of-a-binary-tree/

Given the root of a binary tree, determine if it is a complete binary tree.
A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.

Constraints:
- The number of nodes in the tree is in the range [1, 100].
- 1 <= Node.val <= 1000

Example:
Input: root = [1,2,3,4,5,6]
Output: true
"""
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        end = False
        while queue:
            node = queue.popleft()
            if not node:
                end = True
            else:
                if end:
                    return False
                queue.append(node.left)
                queue.append(node.right)
        return True

# Example usage (constructs tree and checks completeness)
if __name__ == "__main__":
    root = TreeNode(1,
            TreeNode(2, TreeNode(4), TreeNode(5)),
            TreeNode(3, TreeNode(6)))
    print(Solution().isCompleteTree(root))  # Output: True
