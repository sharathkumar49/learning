# 24. Swap Nodes in Pairs
# Given a linked list, swap every two adjacent nodes and return its head.
# You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
#
# Example 1:
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
#
# Example 2:
# Input: head = []
# Output: []
#
# Example 3:
# Input: head = [1]
# Output: [1]
#
# Constraints:
# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    while head and head.next:
        first = head
        second = head.next
        prev.next = second
        first.next = second.next
        second.next = first
        prev = first
        head = first.next
    return dummy.next

# Example usage (helper to print list)
def print_list(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
result = swapPairs(head)
print_list(result)  # Output: 2 1 4 3
