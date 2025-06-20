"""
894. All Possible Full Binary Trees
https://leetcode.com/problems/all-possible-full-binary-trees/

Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.
Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.
A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Constraints:
- 1 <= n <= 20
- n is odd.

Example:
Input: n = 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0]]
"""
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        from functools import lru_cache
        @lru_cache(None)
        def build(m):
            if m == 1:
                return [TreeNode(0)]
            res = []
            for l in range(1, m, 2):
                for left in build(l):
                    for right in build(m - 1 - l):
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        res.append(root)
            return res
        return build(n)

# Example usage (prints number of trees for n=7)
if __name__ == "__main__":
    trees = Solution().allPossibleFBT(7)
    print(len(trees))  # Output: 5
