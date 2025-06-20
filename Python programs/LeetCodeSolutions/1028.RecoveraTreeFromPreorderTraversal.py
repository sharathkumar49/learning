"""
1028. Recover a Tree From Preorder Traversal

We run a preorder depth-first search on the root of a binary tree.
The result of this traversal is represented as a string S of numbers separated by dashes, where dashes represent the depth of the node.
Return the root of the tree.

Constraints:
- 1 <= S.length <= 1000
- S consists of digits, '-' and numbers only.

Example:
Input: S = "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def recoverFromPreorder(S: str) -> Optional[TreeNode]:
    stack = []
    i = 0
    n = len(S)
    while i < n:
        depth = 0
        while i < n and S[i] == '-':
            depth += 1
            i += 1
        val = 0
        while i < n and S[i].isdigit():
            val = val * 10 + int(S[i])
            i += 1
        node = TreeNode(val)
        while len(stack) > depth:
            stack.pop()
        if stack:
            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node
        stack.append(node)
    return stack[0] if stack else None

# Example usage:
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
    while result and result[-1] is None:
        result.pop()
    return result

S = "1-2--3--4-5--6--7"
root = recoverFromPreorder(S)
print(print_level_order(root))  # Output: [1, 2, 5, 3, 4, 6, 7]
