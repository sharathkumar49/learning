# Sort a Linked List (Merge Sort)
# Sort a linked list in O(n log n) time and constant space complexity.
# LeetCode 148
from linked_list_impl import Node, LinkedList

def sort_list(head):
    if not head or not head.next:
        return head
    # Split list
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    slow.next = None
    left = sort_list(head)
    right = sort_list(mid)
    # Merge
    return merge(left, right)

def merge(l1, l2):
    dummy = Node(0)
    tail = dummy
    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next
# Example usage:
ll = LinkedList()
ll.insert_values([4,2,1,3])
ll.head = sort_list(ll.head)
ll.print()  # Output: 1 --> 2 --> 3 --> 4
