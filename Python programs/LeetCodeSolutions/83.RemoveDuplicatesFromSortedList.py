"""
83. Remove Duplicates from Sorted List
https://leetcode.com/problems/remove-duplicates-from-sorted-list/

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Constraints:
- The number of nodes in the list is in the range [0, 300].
- -100 <= Node.val <= 100
- The list is sorted in ascending order.

Example:
Input: head = [1,1,2]
Output: [1,2]
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head

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
    head = list_to_linked([1,1,2])
    result = deleteDuplicates(head)
    print(linked_to_list(result))  # Output: [1,2]
