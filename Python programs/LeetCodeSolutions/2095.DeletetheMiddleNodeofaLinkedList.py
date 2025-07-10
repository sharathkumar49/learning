"""
LeetCode 2095. Delete the Middle Node of a Linked List

Given the head of a linked list, delete the middle node and return the head.

Example:
Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]

Constraints:
- The number of nodes in the list is in the range [1, 10^5].
- 1 <= Node.val <= 10^5
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteMiddle(head):
    if not head or not head.next:
        return None
    slow = head
    fast = head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = slow.next
    return head

# Example usage:
# # Build linked list: 1 -> 3 -> 4 -> 7 -> 1 -> 2 -> 6
# head = ListNode(1, ListNode(3, ListNode(4, ListNode(7, ListNode(1, ListNode(2, ListNode(6)))))))
# res = deleteMiddle(head)
# while res:
#     print(res.val, end=' ')
# # Output: 1 3 4 1 2 6
