"""
LeetCode 1836. Remove Duplicates From an Unsorted Linked List

Given the head of a linked list, remove all duplicates.

Example 1:
Input: head = [1,2,3,1,2,4]
Output: [1,2,3,4]

Constraints:
- The number of nodes in the list is in the range [1, 10^4].
- 1 <= Node.val <= 10^4
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicatesUnsorted(head):
    seen = set()
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    while head:
        if head.val in seen:
            prev.next = head.next
        else:
            seen.add(head.val)
            prev = head
        head = head.next
    return dummy.next

# Example usage:
# head = ListNode(1, ListNode(2, ListNode(3, ListNode(1, ListNode(2, ListNode(4))))))
# deleteDuplicatesUnsorted(head)
# Output: [1,2,3,4]
