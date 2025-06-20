"""
663. Equal Tree Partition
Difficulty: Medium

Given the root of a binary tree, return true if you can partition the tree into two trees with equal sum by removing one edge, otherwise return false.

Example 1:
Input: root = [5,10,10,null,null,2,3]
Output: true

Constraints:
The number of nodes in the tree is in the range [1, 10000].
-10^5 <= Node.val <= 10^5
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def checkEqualTree(root):
    sums = set()
    def sumTree(node):
        if not node:
            return 0
        s = node.val + sumTree(node.left) + sumTree(node.right)
        sums.add(s)
        return s
    total = sumTree(root)
    sums.remove(total)
    return total % 2 == 0 and (total // 2) in sums

# Example usage
# (See LeetCode for binary tree construction examples)
