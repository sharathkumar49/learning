"""
508. Most Frequent Subtree Sum

Given the root of a binary tree, return the most frequent subtree sum. If there is a tie, return all the values with the highest frequency in any order.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -10^5 <= Node.val <= 10^5

Example:
Input: root = [5,2,-3]
Output: [2,-3,4]
"""

from collections import Counter

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> list:
        count = Counter()
        def dfs(node):
            if not node:
                return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            count[s] += 1
            return s
        dfs(root)
        if not count:
            return []
        max_freq = max(count.values())
        return [s for s in count if count[s] == max_freq]

# Example usage:
root = TreeNode(5, TreeNode(2), TreeNode(-3))
sol = Solution()
print(sol.findFrequentTreeSum(root))  # Output: [2, -3, 4]
