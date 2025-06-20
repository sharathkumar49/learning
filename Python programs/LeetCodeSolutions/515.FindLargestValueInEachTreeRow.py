"""
515. Find Largest Value in Each Tree Row

Given the root of a binary tree, return an array of the largest value in each row of the tree.

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- -2^31 <= Node.val <= 2^31 - 1

Example:
Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: TreeNode) -> list:
        if not root:
            return []
        res = []
        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(max(level))
        return res

# Example usage:
root = TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9)))
sol = Solution()
print(sol.largestValues(root))  # Output: [1, 3, 9]
