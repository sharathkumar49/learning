# Reorder List
# Given a singly linked list L: L0→L1→…→Ln-1→Ln, reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
# LeetCode 143
from linked_list_impl import LinkedList, Node

def reorder_list(head):
    if not head or not head.next:
        return head
    # Find middle
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    # Reverse second half
    prev, curr = None, slow.next
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    slow.next = None
    # Merge two halves
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2
    return head
# Example usage:
ll = LinkedList()
ll.insert_values([1,2,3,4,5])
ll.head = reorder_list(ll.head)
ll.print()  # Output: 1 --> 5 --> 2 --> 4 --> 3
