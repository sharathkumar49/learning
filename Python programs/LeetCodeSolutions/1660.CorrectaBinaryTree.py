"""
LeetCode 1660. Correct a Binary Tree

Given the root of a binary tree, return the root after correcting the tree. The tree is incorrect if a right node points to another node at the same level or below.

Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -10^5 <= Node.val <= 10^5
"""

def correctBinaryTree(root):
    from collections import deque
    q = deque([root])
    seen = set()
    while q:
        nxt = deque()
        for node in q:
            if node.right and node.right in seen:
                return node
            nxt.extend(c for c in (node.left, node.right) if c)
        seen |= set(q)
        q = nxt
    return root

# Example usage:
# (Assume TreeNode class is defined)
# root = ...
# print(correctBinaryTree(root))
