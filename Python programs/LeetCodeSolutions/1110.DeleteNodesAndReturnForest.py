"""
1110. Delete Nodes And Return Forest

Given the root of a binary tree and a list of nodes to delete, return the forest after deleting the nodes.

Constraints:
- The number of nodes in the tree is between 1 and 1000.
- Each node has a unique value.
- 1 <= to_delete.length <= 1000
- 1 <= Node.val <= 1000

Example:
Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
"""
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def delNodes(root: Optional[TreeNode], to_delete: List[int]) -> List[Optional[TreeNode]]:
    to_delete_set = set(to_delete)
    res = []
    def helper(node, is_root):
        if not node:
            return None
        root_deleted = node.val in to_delete_set
        if is_root and not root_deleted:
            res.append(node)
        node.left = helper(node.left, root_deleted)
        node.right = helper(node.right, root_deleted)
        return None if root_deleted else node
    helper(root, True)
    return res

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

def print_forest(forest):
    return [[n.val if n else None for n in deque([tree])] for tree in forest]

root = build_tree([1,2,3,4,5,6,7])
to_delete = [3,5]
forest = delNodes(root, to_delete)
print([tree.val for tree in forest])  # Output: [1, 6, 7]
