"""
437. Path Sum III

Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

Constraints:
- The number of nodes in the tree is in the range [0, 1000].
- -10^9 <= Node.val <= 10^9
- -1000 <= targetSum <= 1000

Example:
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def dfs(node, curr_sum):
            if not node:
                return 0
            curr_sum += node.val
            return (prefix.get(curr_sum - targetSum, 0) +
                    dfs(node.left, curr_sum) +
                    dfs(node.right, curr_sum))
        def helper(node, curr_sum):
            if not node:
                return 0
            curr_sum += node.val
            res = prefix.get(curr_sum - targetSum, 0)
            prefix[curr_sum] = prefix.get(curr_sum, 0) + 1
            res += helper(node.left, curr_sum)
            res += helper(node.right, curr_sum)
            prefix[curr_sum] -= 1
            return res
        prefix = {0: 1}
        return helper(root, 0)

# Example usage:
# Construct the tree: 10,5,-3,3,2,null,11,3,-2,null,1
root = TreeNode(10,
    TreeNode(5,
        TreeNode(3, TreeNode(3), TreeNode(-2)),
        TreeNode(2, None, TreeNode(1))
    ),
    TreeNode(-3, None, TreeNode(11))
)
sol = Solution()
print(sol.pathSum(root, 8))  # Output: 3
