"""
LeetCode 2046. Sort Linked List Already Sorted Using Absolute Values

Given the head of a singly linked list sorted by absolute values, return the list sorted by actual values.

Example:
Input: head = [0,2,-5,5,10,-10]
Output: [-10,-5,0,2,5,10]

Constraints:
- The number of nodes in the list is in the range [1, 10^5].
- -10^5 <= Node.val <= 10^5
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortLinkedList(head):
    # Separate negative and non-negative nodes
    neg = None
    pos = None
    curr = head
    while curr:
        nxt = curr.next
        if curr.val < 0:
            curr.next = neg
            neg = curr
        else:
            if pos is None:
                pos = curr
                pos_tail = curr
            else:
                pos_tail.next = curr
                pos_tail = curr
            pos_tail.next = None
        curr = nxt
    # Merge negative and positive lists
    if neg is None:
        return pos
    curr = neg
    while curr.next:
        curr = curr.next
    curr.next = pos
    return neg

# Example usage:
# # Build linked list: 0 -> 2 -> -5 -> 5 -> 10 -> -10
# head = ListNode(0, ListNode(2, ListNode(-5, ListNode(5, ListNode(10, ListNode(-10))))))
# res = sortLinkedList(head)
# while res:
#     print(res.val, end=' ')
# # Output: -10 -5 0 2 5 10
