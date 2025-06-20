"""
662. Maximum Width of Binary Tree
Difficulty: Medium

Given the root of a binary tree, return the maximum width of the given tree. The maximum width of a tree is the maximum width among all levels.

Example 1:
Input: root = [1,3,2,5,3,null,9]
Output: 4

Constraints:
The number of nodes in the tree is in the range [1, 3000].
-100 <= Node.val <= 100
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def widthOfBinaryTree(root):
    from collections import deque
    max_width = 0
    queue = deque([(root, 1)])
    while queue:
        level_length = len(queue)
        _, first = queue[0]
        for _ in range(level_length):
            node, idx = queue.popleft()
            if node.left:
                queue.append((node.left, 2*idx))
            if node.right:
                queue.append((node.right, 2*idx+1))
        max_width = max(max_width, idx - first + 1)
    return max_width

# Example usage
# (See LeetCode for binary tree construction examples)
