"""
919. Complete Binary Tree Inserter
https://leetcode.com/problems/complete-binary-tree-inserter/

A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.
Implement the CBTInserter class:
- CBTInserter(TreeNode root) initializes the data structure with the root of the complete binary tree.
- int insert(int v) inserts a TreeNode into the tree with value v so that the tree remains complete, and returns the value of the parent of the inserted TreeNode.
- TreeNode get_root() returns the root node of the tree.

Constraints:
- The number of nodes in the tree will be in the range [1, 5000].
- 0 <= Node.val <= 5000
- root is a complete binary tree.
- 0 <= v <= 5000

Example:
Input: ["CBTInserter","insert","insert","get_root"], [[[1,2]],[3],[4],[]]
Output: [null,1,2,[1,2,3,4]]
"""
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class CBTInserter:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.deque = deque()
        q = deque([root])
        while q:
            node = q.popleft()
            if not node.left or not node.right:
                self.deque.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def insert(self, v: int) -> int:
        node = self.deque[0]
        new_node = TreeNode(v)
        if not node.left:
            node.left = new_node
        else:
            node.right = new_node
            self.deque.popleft()
        self.deque.append(new_node)
        return node.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root

# Example usage (prints root value after insertions)
if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2))
    cbt = CBTInserter(root)
    print(cbt.insert(3))  # Output: 1
    print(cbt.insert(4))  # Output: 2
    print(cbt.get_root().val)  # Output: 1
