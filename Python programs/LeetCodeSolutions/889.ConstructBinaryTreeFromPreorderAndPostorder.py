"""
889. Construct Binary Tree from Preorder and Postorder Traversal

Given preorder and postorder traversal of a binary tree, construct the tree and return its root.

Example 1:
Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]

Constraints:
- 1 <= preorder.length <= 30
- 1 <= preorder[i], postorder[i] <= 30
- preorder and postorder are valid traversals of the same tree.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def constructFromPrePost(preorder, postorder):
    if not preorder:
        return None
    root = TreeNode(preorder[0])
    if len(preorder) == 1:
        return root
    L = postorder.index(preorder[1]) + 1
    root.left = constructFromPrePost(preorder[1:L+1], postorder[:L])
    root.right = constructFromPrePost(preorder[L+1:], postorder[L:-1])
    return root

# Example usage:
# Helper function to print tree in level order
# ...omitted for brevity...
