"""
938. Range Sum of BST
https://leetcode.com/problems/range-sum-of-bst/

Given the root node of a binary search tree, return the sum of values of all nodes with value in the range [low, high].

Constraints:
- The number of nodes in the tree is in the range [1, 2 * 10^4].
- 1 <= Node.val <= 10^5
- 1 <= low <= high <= 10^5
- All Node.val are unique.

Example:
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        return (root.val +
                self.rangeSumBST(root.left, low, high) +
                self.rangeSumBST(root.right, low, high))

# Example usage (constructs tree and prints sum)
if __name__ == "__main__":
    root = TreeNode(10,
            TreeNode(5, TreeNode(3), TreeNode(7)),
            TreeNode(15, None, TreeNode(18)))
    low = 7
    high = 15
    print(Solution().rangeSumBST(root, low, high))  # Output: 32
