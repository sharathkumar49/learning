"""
1008. Construct Binary Search Tree from Preorder Traversal

Return the root of a binary search tree that matches the given preorder traversal.

Constraints:
- 1 <= preorder.length <= 100
- 1 <= preorder[i] <= 10^8
- The values of preorder are unique.

Example:
Input: preorder = [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]
"""
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bstFromPreorder(preorder: List[int]) -> Optional[TreeNode]:
    def helper(bound=float('inf')):
        nonlocal idx
        if idx == len(preorder) or preorder[idx] > bound:
            return None
        root = TreeNode(preorder[idx])
        idx += 1
        root.left = helper(root.val)
        root.right = helper(bound)
        return root
    idx = 0
    return helper()

# Example usage:
# To print the tree in level order
from collections import deque

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
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    return result

preorder = [8,5,1,7,10,12]
root = bstFromPreorder(preorder)
print(print_level_order(root))  # Output: [8, 5, 10, 1, 7, None, 12]
