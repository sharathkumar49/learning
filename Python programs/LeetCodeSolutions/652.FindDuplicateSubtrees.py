"""
652. Find Duplicate Subtrees
Difficulty: Medium

Given the root of a binary tree, return all duplicate subtrees. For each kind of duplicate subtree, only one of them needs to be returned.

Example 1:
Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]

Constraints:
The number of the nodes in the tree will be in the range [1, 10^4].
-200 <= Node.val <= 200
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findDuplicateSubtrees(root):
    from collections import defaultdict
    res = []
    count = defaultdict(int)
    def serialize(node):
        if not node:
            return '#'
        s = f'{node.val},{serialize(node.left)},{serialize(node.right)}'
        count[s] += 1
        if count[s] == 2:
            res.append(node)
        return s
    serialize(root)
    return res

# Example usage
# (See LeetCode for binary tree construction examples)
