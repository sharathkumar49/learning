"""
LeetCode 725. Split Linked List in Parts

Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

Example 1:
Input: head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]

Example 2:
Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
Output: [[1,2,3,4],[5,6,7],[8,9,10]]

Constraints:
- The number of nodes in the list is in the range [0, 1000].
- 0 <= Node.val <= 1000
- 1 <= k <= 50
"""
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def splitListToParts(head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
    n = 0
    curr = head
    while curr:
        n += 1
        curr = curr.next
    size, extra = divmod(n, k)
    res = []
    curr = head
    for i in range(k):
        dummy = ListNode(0)
        node = dummy
        for j in range(size + (i < extra)):
            node.next = ListNode(curr.val)
            node = node.next
            curr = curr.next if curr else None
        res.append(dummy.next)
    return res

# Example usage
if __name__ == "__main__":
    def build_list(vals):
        dummy = ListNode(0)
        curr = dummy
        for v in vals:
            curr.next = ListNode(v)
            curr = curr.next
        return dummy.next
    def print_parts(parts):
        for part in parts:
            vals = []
            while part:
                vals.append(part.val)
                part = part.next
            print(vals)
    head = build_list([1,2,3])
    print_parts(splitListToParts(head, 5))  # Output: [[1],[2],[3],[],[]]
    head = build_list([1,2,3,4,5,6,7,8,9,10])
    print_parts(splitListToParts(head, 3))  # Output: [[1,2,3,4],[5,6,7],[8,9,10]]
