"""
979. Distribute Coins in Binary Tree
https://leetcode.com/problems/distribute-coins-in-binary-tree/

Given the root of a binary tree with N nodes, each node has a certain number of coins. In one move, you may choose two adjacent nodes and move one coin from one node to another. Return the minimum number of moves required to make every node have exactly one coin.

Constraints:
- The number of nodes in the tree is in the range [1, 100].
- 0 <= Node.val <= 100
- The sum of all Node.val is N.

Example:
Input: root = [3,0,0]
Output: 2
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.moves += abs(left) + abs(right)
            return node.val + left + right - 1
        dfs(root)
        return self.moves

# Example usage (constructs tree and prints moves)
if __name__ == "__main__":
    root = TreeNode(3, TreeNode(0), TreeNode(0))
    print(Solution().distributeCoins(root))  # Output: 2
