"""
109. Convert Sorted List to Binary Search Tree
https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height-balanced binary search tree.

Constraints:
- The number of nodes in the list is in the range [0, 2 * 10^4].
- -10^5 <= Node.val <= 10^5

Example:
Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedListToBST(head: Optional[ListNode]) -> Optional[TreeNode]:
    def find_middle(left, right):
        slow = fast = left
        while fast != right and fast.next != right:
            fast = fast.next.next
            slow = slow.next
        return slow
    def convert(left, right):
        if left == right:
            return None
        mid = find_middle(left, right)
        node = TreeNode(mid.val)
        node.left = convert(left, mid)
        node.right = convert(mid.next, right)
        return node
    return convert(head, None)

# Example usage:
if __name__ == "__main__":
    def list_to_linked(lst):
        dummy = ListNode()
        curr = dummy
        for v in lst:
            curr.next = ListNode(v)
            curr = curr.next
        return dummy.next
    head = list_to_linked([-10,-3,0,5,9])
    root = sortedListToBST(head)
    # Output: BST with root value 0, left child -3, right child 9, etc.
