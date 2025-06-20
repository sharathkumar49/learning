"""
285. Inorder Successor in BST
https://leetcode.com/problems/inorder-successor-in-bst/

Given the root of a binary search tree and a node p, return the inorder successor of node p if it exists, otherwise return null.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -10^5 <= Node.val <= 10^5
- All Node.val are unique.
- p is guaranteed to be in the BST.

Example 1:
Input: root = [2,1,3], p = 1
Output: 2

Example 2:
Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderSuccessor(root, p):
    succ = None
    while root:
        if p.val < root.val:
            succ = root
            root = root.left
        else:
            root = root.right
    return succ

# Example usage:
if __name__ == "__main__":
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    p = root.left
    print(inorderSuccessor(root, p).val if inorderSuccessor(root, p) else None)  # Output: 2
    root2 = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
    p2 = root2.right
    print(inorderSuccessor(root2, p2))  # Output: None
