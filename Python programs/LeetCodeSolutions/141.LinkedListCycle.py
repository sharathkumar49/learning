# 141. Linked List Cycle
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
#
# Example 1:
# Input: head = [3,2,0,-4], pos = 1 (tail connects to node index 1)
# Output: true
#
# Example 2:
# Input: head = [1,2], pos = 0
# Output: true
#
# Example 3:
# Input: head = [1], pos = -1
# Output: false
#
# Constraints:
# The number of nodes in the list is in the range [0, 10^4].
# -10^5 <= Node.val <= 10^5
# pos is -1 or a valid index in the linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Example usage
# (Cycle creation for testing)
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # cycle
print("Has cycle:", hasCycle(node1))  # Output: True
