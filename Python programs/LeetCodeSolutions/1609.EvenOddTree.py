"""
LeetCode 1609. Even Odd Tree

Given a binary tree, return true if the tree is an Even-Odd Tree. A binary tree is Even-Odd if:
- The root is at level 0, and all values at even-indexed levels are odd and strictly increasing.
- All values at odd-indexed levels are even and strictly decreasing.

Example 1:
Input: root = [1,10,4,3,null,7,9,12,8,6,null,null,2]
Output: true

Constraints:
- The number of nodes in the tree is in the range [1, 10^5].
- 1 <= Node.val <= 10^6
"""

def isEvenOddTree(root):
    from collections import deque
    q = deque([root])
    level = 0
    while q:
        prev = None
        for _ in range(len(q)):
            node = q.popleft()
            v = node.val
            if level % 2 == 0:
                if v % 2 == 0 or (prev is not None and v <= prev):
                    return False
            else:
                if v % 2 == 1 or (prev is not None and v >= prev):
                    return False
            prev = v
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1
    return True

# Example usage:
# (Assume TreeNode class is defined)
# root = ...
# print(isEvenOddTree(root))
