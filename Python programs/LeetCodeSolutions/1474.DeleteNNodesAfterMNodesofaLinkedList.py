"""
LeetCode 1474. Delete N Nodes After M Nodes of a Linked List

Given the head of a linked list, delete N nodes after every M nodes of the linked list.

Constraints:
- The number of nodes in the list is in the range [1, 10^4].
- 1 <= M, N <= 1000

Example:
Input: head = [1,2,3,4,5,6,7,8,9,10], M = 2, N = 3
Output: [1,2,6,7]
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteNodes(head, M, N):
    curr = head
    while curr:
        for _ in range(1, M):
            if curr:
                curr = curr.next
        temp = curr
        for _ in range(N):
            if temp and temp.next:
                temp = temp.next
        if curr:
            curr.next = temp.next if temp else None
            curr = curr.next
    return head

# Example usage:
# head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9, ListNode(10))))))))))
# M, N = 2, 3
# new_head = deleteNodes(head, M, N)
# # Output: [1,2,6,7]
