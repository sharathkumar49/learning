"""
Serialize/Deserialize BST (optimized for BST)
"""
from typing import Optional

class TreeNode:
    def __init__(self, val: int, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

class CodecBST:
    def serialize(self, root: Optional[TreeNode]) -> str:
        vals = []
        def preorder(node):
            if node:
                vals.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
        preorder(root)
        return ' '.join(vals)
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = list(map(int, data.split()))
        def build(lower, upper):
            if vals and lower < vals[0] < upper:
                val = vals.pop(0)
                node = TreeNode(val)
                node.left = build(lower, val)
                node.right = build(val, upper)
                return node
            return None
        return build(float('-inf'), float('inf'))
