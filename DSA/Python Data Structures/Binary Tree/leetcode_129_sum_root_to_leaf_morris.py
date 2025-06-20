"""
LeetCode 129: Sum Root to Leaf Numbers (Amazon, Google) [Morris Traversal Version]
Given a binary tree containing digits from 0-9 only, each root-to-leaf path represents a number. Return the total sum of all root-to-leaf numbers (Morris traversal approach).
"""
from typing import Optional

class TreeNode:
    def __init__(self, val: int, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def sum_numbers_morris(root: Optional[TreeNode]) -> int:
    total = 0
    curr = root
    curr_sum = 0
    while curr:
        if not curr.left:
            curr_sum = curr_sum * 10 + curr.val
            if not curr.right and not curr.left:
                total += curr_sum
            curr = curr.right
        else:
            pred = curr.left
            steps = 1
            while pred.right and pred.right != curr:
                pred = pred.right
                steps += 1
            if not pred.right:
                pred.right = curr
                curr_sum = curr_sum * 10 + curr.val
                curr = curr.left
            else:
                pred.right = None
                if not pred.left and not pred.right:
                    total += curr_sum
                for _ in range(steps):
                    curr_sum //= 10
                curr = curr.right
    return total
