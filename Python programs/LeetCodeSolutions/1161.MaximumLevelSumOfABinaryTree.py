"""
1161. Maximum Level Sum of a Binary Tree

Given the root of a binary tree, return the level (1-indexed) with the maximum sum.

Constraints:
- The number of nodes in the tree is between 1 and 10^4.
- -10^5 <= Node.val <= 10^5

Example:
Input: root = [1,7,0,7,-8,null,null]
Output: 2

"""
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxLevelSum(root):
    q = deque([root])
    max_sum = float('-inf')
    level = 0
    ans = 0
    while q:
        level += 1
        s = sum(node.val for node in q)
        if s > max_sum:
            max_sum = s
            ans = level
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return ans

# Example usage
if __name__ == "__main__":
    root = TreeNode(1, TreeNode(7, TreeNode(7), TreeNode(-8)), TreeNode(0))
    print(maxLevelSum(root))  # Output: 2
