"""
LeetCode 2130. Maximum Twin Sum of a Linked List

Given the head of a linked list, return the maximum twin sum of the list.

Example:
Input: head = [5,4,2,1]
Output: 6

Constraints:
- The number of nodes in the list is in the range [1, 10^5].
- 1 <= Node.val <= 10^5
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def pairSum(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    n = len(vals)
    return max(vals[i] + vals[n-1-i] for i in range(n//2))

# Example usage:
# # Build linked list: 5 -> 4 -> 2 -> 1
# head = ListNode(5, ListNode(4, ListNode(2, ListNode(1))))
# print(pairSum(head))  # Output: 6
