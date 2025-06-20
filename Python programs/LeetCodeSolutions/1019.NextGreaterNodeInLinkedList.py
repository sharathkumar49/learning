"""
1019. Next Greater Node In Linked List

You are given the head of a linked list with n nodes. For each node in the list, find the value of the next greater node. If such a node does not exist, set the value to 0.

Constraints:
- 1 <= n <= 10^4
- 1 <= Node.val <= 10^9

Example:
Input: head = [2,1,5]
Output: [5,5,0]
"""
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def nextLargerNodes(head: Optional[ListNode]) -> List[int]:
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    res = [0] * len(vals)
    stack = []
    for i, v in enumerate(vals):
        while stack and vals[stack[-1]] < v:
            res[stack.pop()] = v
        stack.append(i)
    return res

# Example usage:
# Helper to create linked list from list

def create_linked_list(lst):
    dummy = ListNode(0)
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

head = create_linked_list([2,1,5])
print(nextLargerNodes(head))  # Output: [5, 5, 0]
