"""
LeetCode 1602. Find Nearest Right Node in Binary Tree

Given the root of a binary tree and a target node, return the value of the nearest node to the right of the target node in the same level. If there is no such node, return None.

Example 1:
Input: root = [1,2,3,null,4,5,6], target = 4
Output: 5

Constraints:
- The number of nodes in the tree is in the range [1, 10^5].
- 1 <= Node.val <= 10^5
"""

def findNearestRightNode(root, target):
    from collections import deque
    q = deque([root])
    while q:
        size = len(q)
        for i in range(size):
            node = q.popleft()
            if node == target:
                return q[0] if i < size - 1 else None
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return None

# Example usage:
# (Assume TreeNode class is defined)
# root = ...
# target = ...
# print(findNearestRightNode(root, target))
