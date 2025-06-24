"""
LeetCode 1302. Deepest Leaves Sum

Given the root of a binary tree, return the sum of the values of its deepest leaves.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- 1 <= Node.val <= 100

Example:
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deepestLeavesSum(root):
    from collections import deque
    queue = deque([root])
    while queue:
        level_sum = 0
        for _ in range(len(queue)):
            node = queue.popleft()
            level_sum += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return level_sum

# Example usage:
# root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(7)), TreeNode(5)), TreeNode(3, None, TreeNode(6, None, TreeNode(8))))
# print(deepestLeavesSum(root))  # Output: 15
