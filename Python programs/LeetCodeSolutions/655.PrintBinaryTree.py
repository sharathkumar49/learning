"""
655. Print Binary Tree
Difficulty: Medium

Given the root of a binary tree, return a 2D string array where each row represents a level of the tree and each column represents a position in the tree. The width of the array should be 2^height - 1.

Example 1:
Input: root = [1,2]
Output: [["","1",""],["2","",""]]

Constraints:
The number of nodes in the tree is in the range [1, 2^10].
-99 <= Node.val <= 99
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def printTree(root):
    def height(node):
        return 1 + max(height(node.left), height(node.right)) if node else 0
    h = height(root)
    w = 2 ** h - 1
    res = [[''] * w for _ in range(h)]
    def fill(node, r, l, rgt):
        if not node:
            return
        m = (l + rgt) // 2
        res[r][m] = str(node.val)
        fill(node.left, r+1, l, m-1)
        fill(node.right, r+1, m+1, rgt)
    fill(root, 0, 0, w-1)
    return res

# Example usage
# (See LeetCode for binary tree construction examples)
