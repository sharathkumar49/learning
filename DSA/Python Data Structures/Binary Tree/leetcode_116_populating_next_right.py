"""
LeetCode 116: Populating Next Right Pointers in Each Node (Microsoft, Amazon)
Given a perfect binary tree, populate each next pointer to point to its next right node.
"""
from typing import Optional

class Node:
    def __init__(self, val: int, left: 'Optional[Node]' = None, right: 'Optional[Node]' = None, next: 'Optional[Node]' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect(root: Optional[Node]) -> Optional[Node]:
    if not root:
        return None
    leftmost = root
    while leftmost.left:
        head = leftmost
        while head:
            head.left.next = head.right
            if head.next:
                head.right.next = head.next.left
            head = head.next
        leftmost = leftmost.left
    return root
