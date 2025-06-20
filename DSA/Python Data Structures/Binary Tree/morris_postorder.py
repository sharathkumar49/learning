"""
Morris Postorder Traversal (O(1) space)
Prints the postorder traversal of a binary tree using Morris Traversal.
"""
from typing import Optional, List

class TreeNode:
    def __init__(self, val: int, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def morris_postorder(root: Optional[TreeNode]) -> List[int]:
    def reverse_path(start, end):
        if start == end:
            return
        x, y = start, start.right
        while True:
            z = y.right
            y.right = x
            x = y
            y = z
            if x == end:
                break
    def print_reverse(start, end, res):
        reverse_path(start, end)
        node = end
        while True:
            res.append(node.val)
            if node == start:
                break
            node = node.right
        reverse_path(end, start)
    dummy = TreeNode(0)
    dummy.left = root
    curr = dummy
    res = []
    while curr:
        if not curr.left:
            curr = curr.right
        else:
            pred = curr.left
            while pred.right and pred.right != curr:
                pred = pred.right
            if not pred.right:
                pred.right = curr
                curr = curr.left
            else:
                print_reverse(curr.left, pred, res)
                pred.right = None
                curr = curr.right
    return res
