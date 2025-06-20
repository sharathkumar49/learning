"""
250. Count Univalue Subtrees
https://leetcode.com/problems/count-univalue-subtrees/

Given the root of a binary tree, return the number of uni-value subtrees.
A uni-value subtree means all nodes of the subtree have the same value.

Constraints:
- The number of the node in the tree will be in the range [0, 1000].
- -1000 <= Node.val <= 1000

Example 1:
Input: root = [5,1,5,5,5,null,5]
Output: 4

Example 2:
Input: root = []
Output: 0
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def countUnivalSubtrees(root):
    def is_unival(node, parent_val):
        if not node:
            return True
        left = is_unival(node.left, node.val)
        right = is_unival(node.right, node.val)
        if left and right:
            count[0] += 1
            return node.val == parent_val
        return False
    count = [0]
    is_unival(root, None)
    return count[0]

# Example usage:
if __name__ == "__main__":
    root = TreeNode(5, TreeNode(1, TreeNode(5), TreeNode(5)), TreeNode(5, None, TreeNode(5)))
    print(countUnivalSubtrees(root))  # Output: 4
    print(countUnivalSubtrees(None))  # Output: 0
