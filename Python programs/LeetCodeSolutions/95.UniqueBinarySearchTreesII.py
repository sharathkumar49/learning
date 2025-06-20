"""
95. Unique Binary Search Trees II
https://leetcode.com/problems/unique-binary-search-trees-ii/

Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

Constraints:
- 1 <= n <= 8

Example:
Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,1]]
"""
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def generateTrees(n: int) -> List[Optional[TreeNode]]:
    def build(l, r):
        if l > r:
            return [None]
        res = []
        for i in range(l, r+1):
            for left in build(l, i-1):
                for right in build(i+1, r):
                    node = TreeNode(i)
                    node.left = left
                    node.right = right
                    res.append(node)
        return res
    return build(1, n) if n else []

# Example usage:
if __name__ == "__main__":
    def serialize(root):
        res = []
        def preorder(node):
            if not node:
                res.append(None)
                return
            res.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return res
    trees = generateTrees(3)
    for t in trees:
        print(serialize(t))
