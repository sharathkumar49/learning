"""
897. Increasing Order Search Tree
https://leetcode.com/problems/increasing-order-search-tree/

Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

Constraints:
- The number of nodes in the given tree will be in the range [1, 100].
- 0 <= Node.val <= 100

Example:
Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node] + inorder(node.right)
        nodes = inorder(root)
        for i in range(len(nodes)):
            nodes[i].left = None
            nodes[i].right = nodes[i+1] if i+1 < len(nodes) else None
        return nodes[0] if nodes else None

# Example usage (constructs tree and prints in-order traversal)
if __name__ == "__main__":
    def build_tree():
        n1 = TreeNode(1)
        n2 = TreeNode(2, n1)
        n4 = TreeNode(4)
        n3 = TreeNode(3, n2, n4)
        n7 = TreeNode(7)
        n9 = TreeNode(9)
        n8 = TreeNode(8, n7, n9)
        n6 = TreeNode(6, None, n8)
        n5 = TreeNode(5, n3, n6)
        return n5
    def print_inorder(node):
        if node:
            print(node.val, end=' ')
            print_inorder(node.right)
    root = build_tree()
    new_root = Solution().increasingBST(root)
    print_inorder(new_root)  # Output: 1 2 3 4 5 6 7 8 9
