"""
160. Intersection of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists/

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection, return null.

Constraints:
- The number of nodes in each list is in the range [0, 3 * 10^4].
- -10^5 <= Node.val <= 10^5

Example:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5]
Output: Intersected at '8'
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getIntersectionNode(headA: Optional[ListNode], headB: Optional[ListNode]) -> Optional[ListNode]:
    if not headA or not headB:
        return None
    a, b = headA, headB
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a

# Example usage:
if __name__ == "__main__":
    # Example: intersection at node with value 8
    a1 = ListNode(4)
    a2 = ListNode(1)
    c1 = ListNode(8)
    c2 = ListNode(4)
    c3 = ListNode(5)
    b1 = ListNode(5)
    b2 = ListNode(6)
    b3 = ListNode(1)
    a1.next = a2
    a2.next = c1
    c1.next = c2
    c2.next = c3
    b1.next = b2
    b2.next = b3
    b3.next = c1
    print(getIntersectionNode(a1, b1) == c1)  # Output: True
