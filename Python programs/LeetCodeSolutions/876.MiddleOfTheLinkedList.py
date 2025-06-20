# 876. Middle of the Linked List
# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.
#
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
#
# Example 2:
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
#
# Constraints:
# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# Example usage (helper to print list)
def print_list(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
mid = middleNode(head)
print_list(mid)  # Output: 3 4 5
