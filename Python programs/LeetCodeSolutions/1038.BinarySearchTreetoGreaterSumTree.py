"""
1038. Binary Search Tree to Greater Sum Tree

Given the root of a Binary Search Tree (BST), convert it to a Greater Sum Tree where every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

Constraints:
- The number of nodes in the tree is between 1 and 100.
- 0 <= Node.val <= 100

Example:
Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bstToGst(root: Optional[TreeNode]) -> Optional[TreeNode]:
    total = 0
    def reverse_inorder(node):
        nonlocal total
        if node:
            reverse_inorder(node.right)
            total += node.val
            node.val = total
            reverse_inorder(node.left)
    reverse_inorder(root)
    return root

# Example usage:
from collections import deque

def build_tree(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = deque([root])
    i = 1
    while queue and i < len(lst):
        node = queue.popleft()
        if i < len(lst) and lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1
    return root

def print_level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result

root = build_tree([4,1,6,0,2,5,7,None,None,None,3,None,None,None,8])
bstToGst(root)
print(print_level_order(root))  # Output: [30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None, None, 8]
