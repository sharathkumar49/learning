"""
LeetCode 2074. Reverse Nodes in Even Length Groups

Given the head of a linked list, reverse the nodes of the list k at a time for each group of size k, where k increases by 1 each time, and reverse only if the group length is even.

Example:
Input: head = [1,2,3,4,5,6], Output: [1,3,2,6,5,4]

Constraints:
- The number of nodes in the list is in the range [1, 10^5].
- 1 <= Node.val <= 10^5
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseEvenLengthGroups(head):
    dummy = ListNode(0, head)
    prev = dummy
    k = 1
    while head:
        cnt = 0
        node = head
        while node and cnt < k:
            node = node.next
            cnt += 1
        if cnt % 2 == 0:
            prev2 = prev
            curr = head
            for _ in range(cnt):
                nxt = curr.next
                curr.next = prev2.next
                prev2.next = curr
                curr = nxt
            head.next = curr
            prev = head
            head = curr
        else:
            for _ in range(cnt):
                prev = head
                head = head.next
        k += 1
    return dummy.next

# Example usage:
# # Build linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6
# head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
# res = reverseEvenLengthGroups(head)
# while res:
#     print(res.val, end=' ')
# # Output: 1 3 2 6 5 4
