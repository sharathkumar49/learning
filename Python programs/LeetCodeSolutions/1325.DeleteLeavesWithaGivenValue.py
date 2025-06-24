"""
LeetCode 1325. Delete Leaves With a Given Value

Given the root of a binary tree and an integer target, delete all the leaf nodes with value target. If after deleting such leaves, new leaves are formed with the value target, delete them as well.

Constraints:
- The number of nodes in the tree is in the range [1, 3000].
- 1 <= Node.val, target <= 1000

Example:
Input: root = [1,2,3,2,null,2,4], target = 2
Output: [1,null,3,null,4]
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def removeLeafNodes(root, target):
    if not root:
        return None
    root.left = removeLeafNodes(root.left, target)
    root.right = removeLeafNodes(root.right, target)
    if not root.left and not root.right and root.val == target:
        return None
    return root

# Example usage:
# root = TreeNode(1, TreeNode(2, TreeNode(2)), TreeNode(3, TreeNode(2), TreeNode(4)))
# target = 2
# print(removeLeafNodes(root, target))
