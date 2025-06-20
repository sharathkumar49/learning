"""
369. Plus One Linked List

Given the head of a singly linked list representing a non-negative integer, plus one to the integer and return the head of the resulting linked list.

Constraints:
- The number of nodes in the linked list is in the range [1, 100].
- 0 <= Node.val <= 9
- The number represented by the linked list does not contain leading zeros except for the zero itself.
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def plusOne(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def dfs(node):
            if not node:
                return 1
            carry = dfs(node.next)
            val = node.val + carry
            node.val = val % 10
            return val // 10
        if dfs(head):
            new_head = ListNode(1)
            new_head.next = head
            return new_head
        return head

# Example usage:
# head = ListNode(1, ListNode(2, ListNode(3)))
# new_head = Solution().plusOne(head)
# while new_head:
#     print(new_head.val, end=' ')
#     new_head = new_head.next
# Output: 1 2 4
