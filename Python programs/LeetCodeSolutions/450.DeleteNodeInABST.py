"""
450. Delete Node in a BST

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- -10^5 <= Node.val <= 10^5
- Each node has a unique value.

Example:
Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            min_larger_node = root.right
            while min_larger_node.left:
                min_larger_node = min_larger_node.left
            root.val = min_larger_node.val
            root.right = self.deleteNode(root.right, min_larger_node.val)
        return root

# Example usage:
# Construct BST: 5,3,6,2,4,null,7
root = TreeNode(5,
    TreeNode(3, TreeNode(2), TreeNode(4)),
    TreeNode(6, None, TreeNode(7))
)
sol = Solution()
root = sol.deleteNode(root, 3)
print(root.left.val)  # Output: 4
