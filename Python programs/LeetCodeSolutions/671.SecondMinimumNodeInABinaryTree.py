"""
LeetCode 671. Second Minimum Node In a Binary Tree

Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.
If no such second minimum value exists, output -1 instead.

Example 1:
Input: root = [2,2,5,null,null,5,7]
Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.

Example 2:
Input: root = [2,2,2]
Output: -1
Explanation: The smallest value is 2, but there isn't any second minimum value.

Constraints:
- The number of nodes in the tree is in the range [1, 25].
- 1 <= Node.val <= 2^31 - 1
- root.val == min(root.left.val, root.right.val) for each internal node of the tree.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findSecondMinimumValue(root: Optional[TreeNode]) -> int:
    vals = set()
    def dfs(node):
        if node:
            vals.add(node.val)
            dfs(node.left)
            dfs(node.right)
    dfs(root)
    min_val = min(vals)
    vals = [v for v in vals if v != min_val]
    return min(vals) if vals else -1

# Example usage
if __name__ == "__main__":
    # Helper to build tree for testing
    def build_tree(vals):
        nodes = [TreeNode(v) if v is not None else None for v in vals]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root
    root = build_tree([2,2,5,None,None,5,7])
    print(findSecondMinimumValue(root))  # Output: 5
    root = build_tree([2,2,2])
    print(findSecondMinimumValue(root))  # Output: -1
