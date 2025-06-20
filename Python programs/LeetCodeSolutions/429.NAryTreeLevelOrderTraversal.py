"""
429. N-ary Tree Level Order Traversal

Given an n-ary tree, return the level order traversal of its nodes' values.

Constraints:
- The height of the n-ary tree is less than or equal to 1000
- The total number of nodes is between [0, 10^4]

Example:
Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]

"""

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def levelOrder(self, root: 'Node'):
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            level = []
            next_queue = []
            for node in queue:
                level.append(node.val)
                next_queue.extend(node.children)
            res.append(level)
            queue = next_queue
        return res

# Example usage:
root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
sol = Solution()
print(sol.levelOrder(root))  # Output: [[1], [3, 2, 4], [5, 6]]
