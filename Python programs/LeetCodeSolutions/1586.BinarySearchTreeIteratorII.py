"""
LeetCode 1586. Binary Search Tree Iterator II

Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST). The iterator is initialized with the root node of a BST. Implement the following methods:
- hasNext(): Returns true if there exists a number in the traversal to the right of the pointer.
- next(): Moves the pointer to the right, then returns the number at the pointer.
- hasPrev(): Returns true if there exists a number in the traversal to the left of the pointer.
- prev(): Moves the pointer to the left, then returns the number at the pointer.

Example:
Input: root = [7,3,15,null,null,9,20]
Output: [null,true,3,true,7,true,9,true,15,true,20,true,15,true,9,true,7,true,3]

Constraints:
- The number of nodes in the tree is in the range [1, 10^5].
- 0 <= Node.val <= 10^6
"""

class BSTIterator:
    def __init__(self, root):
        self.arr = []
        self.idx = -1
        self._inorder(root)
    def _inorder(self, node):
        if not node:
            return
        self._inorder(node.left)
        self.arr.append(node.val)
        self._inorder(node.right)
    def hasNext(self):
        return self.idx + 1 < len(self.arr)
    def next(self):
        self.idx += 1
        return self.arr[self.idx]
    def hasPrev(self):
        return self.idx > 0
    def prev(self):
        self.idx -= 1
        return self.arr[self.idx]
