"""
637. Average of Levels in Binary Tree
Difficulty: Easy

Given the root of a binary tree, return the average value of the nodes on each level in the form of an array.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [10.0, 15.0, 11.0]

Constraints:
The number of nodes in the tree is in the range [1, 10^4].
-2^31 <= Node.val <= 2^31 - 1
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def averageOfLevels(root):
    from collections import deque
    res = []
    queue = deque([root])
    while queue:
        level = [node.val for node in queue]
        res.append(sum(level) / len(level))
        next_queue = deque()
        for node in queue:
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)
        queue = next_queue
    return res

# Example usage
# (See LeetCode for binary tree construction examples)
