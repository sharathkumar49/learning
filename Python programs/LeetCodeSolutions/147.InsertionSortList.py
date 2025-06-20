"""
147. Insertion Sort List
https://leetcode.com/problems/insertion-sort-list/

Given the head of a singly linked list, sort the list using insertion sort and return its head.

Constraints:
- The number of nodes in the list is in the range [0, 5 * 10^4].
- -5 * 10^4 <= Node.val <= 5 * 10^4

Example:
Input: head = [4,2,1,3]
Output: [1,2,3,4]
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insertionSortList(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(float('-inf'))
    curr = head
    while curr:
        prev = dummy
        while prev.next and prev.next.val < curr.val:
            prev = prev.next
        next_temp = curr.next
        curr.next = prev.next
        prev.next = curr
        curr = next_temp
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
    head = list_to_linked([4,2,1,3])
    sorted_head = insertionSortList(head)
    print(linked_to_list(sorted_head))  # Output: [1,2,3,4]
