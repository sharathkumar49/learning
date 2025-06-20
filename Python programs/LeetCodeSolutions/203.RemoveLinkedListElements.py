"""
203. Remove Linked List Elements
https://leetcode.com/problems/remove-linked-list-elements/

Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Constraints:
- The number of nodes in the list is in the range [0, 10^4].
- 1 <= Node.val <= 50
- 0 <= val <= 50

Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:
Input: head = [], val = 1
Output: []

Example 3:
Input: head = [7,7,7,7], val = 7
Output: []
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head, val):
    dummy = ListNode(0)
    dummy.next = head
    curr = dummy
    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return dummy.next

# Example usage:
if __name__ == "__main__":
    def to_list(head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res
    # [1,2,6,3,4,5,6], val = 6
    n = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
    print(to_list(removeElements(n, 6)))  # Output: [1,2,3,4,5]
    print(to_list(removeElements(None, 1)))  # Output: []
    n2 = ListNode(7, ListNode(7, ListNode(7, ListNode(7))))
    print(to_list(removeElements(n2, 7)))  # Output: []
