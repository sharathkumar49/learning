"""
LeetCode 1290. Convert Binary Number in a Linked List to Integer

Given head which is a reference node to a singly-linked list, where each node has a value 0 or 1, return the decimal value of the number in the linked list.

Constraints:
- The Linked List is not empty.
- Number of nodes will not exceed 30.
- Each node's value is either 0 or 1.

Example:
Input: head = [1,0,1]
Output: 5
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getDecimalValue(head):
    num = 0
    while head:
        num = num * 2 + head.val
        head = head.next
    return num

# Example usage:
# head = ListNode(1, ListNode(0, ListNode(1)))
# print(getDecimalValue(head))  # Output: 5
