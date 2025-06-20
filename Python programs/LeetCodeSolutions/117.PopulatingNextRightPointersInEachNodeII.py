"""
117. Populating Next Right Pointers in Each Node II
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

Given a binary tree, populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Constraints:
- The number of nodes in the tree is in the range [0, 6000].
- -100 <= Node.val <= 100

Example:
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
"""
from typing import Optional

class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect(root: Optional[Node]) -> Optional[Node]:
    if not root:
        return None
    queue = [root]
    while queue:
        size = len(queue)
        prev = None
        for _ in range(size):
            node = queue.pop(0)
            if prev:
                prev.next = node
            prev = node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        prev.next = None
    return root

# Example usage:
if __name__ == "__main__":
    # Example tree construction and connection
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n7 = Node(7)
    n1.left, n1.right = n2, n3
    n2.left, n2.right = n4, n5
    n3.right = n7
    connect(n1)
    # n1, n2, n3, n4, n5, n7 now have their .next pointers set
