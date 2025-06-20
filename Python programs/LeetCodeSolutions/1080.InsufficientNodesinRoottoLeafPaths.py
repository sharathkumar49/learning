"""
1080. Insufficient Nodes in Root to Leaf Paths

Given the root of a binary tree and an integer limit, delete all insufficient nodes in the tree. A node is insufficient if every root-to-leaf path containing that node has a sum strictly less than limit.

Constraints:
- The number of nodes in the tree is in the range [1, 5000].
- -10^5 <= Node.val <= 10^5
- -10^9 <= limit <= 10^9

Example:
Input: root = [1,2,-3,-5,None,4,None], limit = -1
Output: [1,2,4]
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sufficientSubset(root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
    def dfs(node, curr_sum):
        if not node:
            return None
        curr_sum += node.val
        if not node.left and not node.right:
            return node if curr_sum >= limit else None
        node.left = dfs(node.left, curr_sum)
        node.right = dfs(node.right, curr_sum)
        return node if node.left or node.right else None
    return dfs(root, 0)

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

root = build_tree([1,2,-3,-5,None,4,None])
limit = -1
root = sufficientSubset(root, limit)
print(print_level_order(root))  # Output: [1, 2, 4]
