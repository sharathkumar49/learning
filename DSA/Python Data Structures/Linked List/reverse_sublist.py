# Reverse a Sublist (Between Positions m and n)
# Reverse a portion of the linked list from position m to n (1-indexed).
from linked_list_impl import Node, LinkedList

def reverse_between(head, m, n):
    if m == n:
        return head
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    for _ in range(m - 1):
        prev = prev.next
    curr = prev.next
    for _ in range(n - m):
        temp = curr.next
        curr.next = temp.next
        temp.next = prev.next
        prev.next = temp
    return dummy.next

# Example usage:
ll = LinkedList()
ll.insert_values([1,2,3,4,5])
ll.head = reverse_between(ll.head, 2, 4)
ll.print()  # Output: 1 --> 4 --> 3 --> 2 --> 5
