"""
Comprehensive Binary Tree and Binary Search Tree Problems
Author: [Your Name]
Date: 2025-06-15

This file contains classic and advanced problems for binary trees and BSTs, with both recursive and iterative solutions where appropriate.
"""

from collections import deque
from typing import Optional, List

# --- Core Binary Tree Node ---
class TreeNode:
    def __init__(self, val: int, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

# --- 1. Inorder / Preorder / Postorder Traversals (Recursive & Iterative) ---

def inorder_recursive(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    return inorder_recursive(root.left) + [root.val] + inorder_recursive(root.right)

def inorder_iterative(root: Optional[TreeNode]) -> List[int]:
    stack, res = [], []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    return res

def preorder_recursive(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    return [root.val] + preorder_recursive(root.left) + preorder_recursive(root.right)

def preorder_iterative(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    stack, res = [root], []
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res

def postorder_recursive(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    return postorder_recursive(root.left) + postorder_recursive(root.right) + [root.val]

def postorder_iterative(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    stack, res = [root], []
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return res[::-1]

# --- 2. Level Order Traversal (BFS) ---
def level_order_traversal(root: Optional[TreeNode]) -> List[List[int]]:
    res = []
    if not root:
        return res
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(level)
    return res

# --- 3. Diameter of a Binary Tree ---
def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    diameter = 0
    def depth(node):
        nonlocal diameter
        if not node:
            return 0
        left = depth(node.left)
        right = depth(node.right)
        diameter = max(diameter, left + right)
        return 1 + max(left, right)
    depth(root)
    return diameter

# --- 4. Check if a Tree is Balanced ---
def is_balanced(root: Optional[TreeNode]) -> bool:
    def check(node):
        if not node:
            return 0, True
        lh, lb = check(node.left)
        rh, rb = check(node.right)
        return 1 + max(lh, rh), lb and rb and abs(lh - rh) <= 1
    return check(root)[1]

# --- 4b. Check if a Tree is Symmetric ---
def is_symmetric(root: Optional[TreeNode]) -> bool:
    def is_mirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return t1.val == t2.val and is_mirror(t1.left, t2.right) and is_mirror(t1.right, t2.left)
    return is_mirror(root, root)

# --- 5. Lowest Common Ancestor (LCA) ---
def lowest_common_ancestor(root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    if not root or root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    return left or right

# --- 6. Maximum Path Sum ---
def max_path_sum(root: Optional[TreeNode]) -> int:
    max_sum = float('-inf')
    def helper(node):
        nonlocal max_sum
        if not node:
            return 0
        left = max(helper(node.left), 0)
        right = max(helper(node.right), 0)
        max_sum = max(max_sum, node.val + left + right)
        return node.val + max(left, right)
    helper(root)
    return max_sum

# --- BST-Specific Problems ---
# Use your BinarySearchTreeNode for these

# 1. Validate a BST

def is_valid_bst(root: Optional[TreeNode], low=float('-inf'), high=float('inf')) -> bool:
    if not root:
        return True
    if not (low < root.val < high):
        return False
    return is_valid_bst(root.left, low, root.val) and is_valid_bst(root.right, root.val, high)

# 3. Kth Smallest Element in BST

def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    stack = []
    curr = root
    while True:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        k -= 1
        if k == 0:
            return curr.val
        curr = curr.right

# 4. Floor and Ceil in a BST

def floor_in_bst(root: Optional[TreeNode], key: int) -> Optional[int]:
    floor = None
    while root:
        if root.val == key:
            return root.val
        if root.val > key:
            root = root.left
        else:
            floor = root.val
            root = root.right
    return floor

def ceil_in_bst(root: Optional[TreeNode], key: int) -> Optional[int]:
    ceil = None
    while root:
        if root.val == key:
            return root.val
        if root.val < key:
            root = root.right
        else:
            ceil = root.val
            root = root.left
    return ceil

# 5. Convert Sorted Array to BST

def sorted_array_to_bst(nums: List[int]) -> Optional[TreeNode]:
    if not nums:
        return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sorted_array_to_bst(nums[:mid])
    root.right = sorted_array_to_bst(nums[mid+1:])
    return root

# 6. BST to Doubly Linked List (in-place)

def bst_to_dll(root: Optional[TreeNode]) -> Optional[TreeNode]:
    def helper(node):
        nonlocal last, head
        if not node:
            return
        helper(node.left)
        if last:
            last.right = node
            node.left = last
        else:
            head = node
        last = node
        helper(node.right)
    last, head = None, None
    helper(root)
    return head

# --- Applications & Patterns ---
# 1. Morris Traversal (Inorder, O(1) space)
def morris_inorder(root: Optional[TreeNode]) -> List[int]:
    res = []
    curr = root
    while curr:
        if not curr.left:
            res.append(curr.val)
            curr = curr.right
        else:
            pre = curr.left
            while pre.right and pre.right != curr:
                pre = pre.right
            if not pre.right:
                pre.right = curr
                curr = curr.left
            else:
                pre.right = None
                res.append(curr.val)
                curr = curr.right
    return res

# 2. BST Iterator
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._push_left(root)
    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left
    def hasNext(self) -> bool:
        return bool(self.stack)
    def next(self) -> int:
        node = self.stack.pop()
        val = node.val
        self._push_left(node.right)
        return val

# 3. Trim BST
def trim_bst(root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
    if not root:
        return None
    if root.val < low:
        return trim_bst(root.right, low, high)
    if root.val > high:
        return trim_bst(root.left, low, high)
    root.left = trim_bst(root.left, low, high)
    root.right = trim_bst(root.right, low, high)
    return root

# 4. Recover BST (Two Nodes Swapped)
def recover_bst(root: Optional[TreeNode]):
    x = y = pred = prev = None
    stack = []
    curr = root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        if prev and curr.val < prev.val:
            y = curr
            if not x:
                x = prev
            else:
                break
        prev = curr
        curr = curr.right
    if x and y:
        x.val, y.val = y.val, x.val

# End of file
