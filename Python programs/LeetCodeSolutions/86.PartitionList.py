"""
86. Partition List
https://leetcode.com/problems/partition-list/

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.

Constraints:
- The number of nodes in the list is in the range [0, 200].
- -100 <= Node.val <= 100
- -200 <= x <= 200

Example:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    before_head = ListNode(0)
    before = before_head
    after_head = ListNode(0)
    after = after_head
    while head:
        if head.val < x:
            before.next = head
            before = before.next
        else:
            after.next = head
            after = after.next
        head = head.next
    after.next = None
    before.next = after_head.next
    return before_head.next

# Example usage:
if __name__ == "__main__":
    def list_to_linked(lst):
        dummy = ListNode()
        curr = dummy
        for v in lst:
            curr.next = ListNode(v)
            curr = curr.next
        return dummy.next
    def linked_to_list(node):
        res = []
        while node:
            res.append(node.val)
            node = node.next
        return res
    head = list_to_linked([1,4,3,2,5,2])
    result = partition(head, 3)
    print(linked_to_list(result))  # Output: [1,2,2,4,3,5]
