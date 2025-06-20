"""
426. Convert Binary Search Tree to Sorted Doubly Linked List

Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.
You can think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.
Let's call the left and right pointers as prev and next in this problem.

We want to transform this BST into a circular doubly linked list. Each node in a doubly linked list has a predecessor and successor. The predecessor of a node is the next smaller node in the order, and the successor is the next larger node in the order. The successor of the largest node is the smallest node, and the predecessor of the smallest node is the largest node.

Constraints:
- The number of nodes in the tree is in the range [0, 2000].
- -1000 <= Node.val <= 1000
- All the values of the tree are unique.

Example:
Input: root = [4,2,5,1,3]
Output: [1,2,3,4,5] (as a circular doubly linked list)

"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        def inorder(node):
            nonlocal last, first
            if node:
                inorder(node.left)
                if last:
                    last.right = node
                    node.left = last
                else:
                    first = node
                last = node
                inorder(node.right)
        first, last = None, None
        inorder(root)
        # Close the circular doubly linked list
        last.right = first
        first.left = last
        return first

# Example usage:
# Construct BST: 4,2,5,1,3
root = Node(4, Node(2, Node(1), Node(3)), Node(5))
sol = Solution()
head = sol.treeToDoublyList(root)
# Print the values in the circular doubly linked list
res = []
curr = head
for _ in range(5):
    res.append(curr.val)
    curr = curr.right
print(res)  # Output: [1, 2, 3, 4, 5]
