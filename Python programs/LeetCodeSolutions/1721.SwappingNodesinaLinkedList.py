"""
LeetCode 1721. Swapping Nodes in a Linked List

Given the head of a linked list and an integer k, swap the values of the kth node from the beginning and the kth node from the end.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

Constraints:
- The number of nodes in the list is n.
- 1 <= k <= n <= 10^5
- 0 <= Node.val <= 100
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapNodes(head, k):
    first = last = head
    for _ in range(k-1):
        first = first.next
    fast = first
    while fast.next:
        fast = fast.next
        last = last.next
    first.val, last.val = last.val, first.val
    return head

# Example usage:
# head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# k = 2
# swapNodes(head, k)
# Output: [1,4,3,2,5]
