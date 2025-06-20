"""
82. Remove Duplicates from Sorted List II
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

Constraints:
- The number of nodes in the list is in the range [0, 300].
- -100 <= Node.val <= 100
- The list is sorted in ascending order.

Example:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    prev = dummy
    while head:
        if head.next and head.val == head.next.val:
            while head.next and head.val == head.next.val:
                head = head.next
            prev.next = head.next
        else:
            prev = prev.next
        head = head.next
    return dummy.next

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
    head = list_to_linked([1,2,3,3,4,4,5])
    result = deleteDuplicates(head)
    print(linked_to_list(result))  # Output: [1,2,5]
