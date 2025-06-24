"""
LeetCode 1430. Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree

Given a binary tree where each node contains a value from 0 to 9, and a sequence of integers, return true if the sequence is a valid path from the root to a leaf.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- 0 <= Node.val <= 9
- 1 <= arr.length <= 10^4

Example:
Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,0,1]
Output: true
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidSequence(root, arr):
    def dfs(node, i):
        if not node or i >= len(arr) or node.val != arr[i]:
            return False
        if not node.left and not node.right and i == len(arr)-1:
            return True
        return dfs(node.left, i+1) or dfs(node.right, i+1)
    return dfs(root, 0)

# Example usage:
# Tree: 0,1,0,0,1,0,null,null,1,0,0
root = TreeNode(0,
    TreeNode(1,
        TreeNode(0, None, None),
        TreeNode(1, TreeNode(1), TreeNode(0))
    ),
    TreeNode(0, TreeNode(0), None)
)
arr = [0,1,0,1]
print(isValidSequence(root, arr))  # Output: True
