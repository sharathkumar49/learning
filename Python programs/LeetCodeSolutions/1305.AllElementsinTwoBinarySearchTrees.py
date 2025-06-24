"""
LeetCode 1305. All Elements in Two Binary Search Trees

Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.

Constraints:
- The number of nodes in each tree is in the range [0, 5000].
- -10^5 <= Node.val <= 10^5

Example:
Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getAllElements(root1, root2):
    def inorder(node):
        return inorder(node.left) + [node.val] + inorder(node.right) if node else []
    return sorted(inorder(root1) + inorder(root2))

# Example usage:
# root1 = TreeNode(2, TreeNode(1), TreeNode(4))
# root2 = TreeNode(1, TreeNode(0), TreeNode(3))
# print(getAllElements(root1, root2))  # Output: [0,1,1,2,3,4]
