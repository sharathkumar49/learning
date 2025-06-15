# Merge Two Sorted Linked Lists
from linked_list_impl import Node, LinkedList

def merge_two_sorted_lists(l1, l2):
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
ll1 = LinkedList(); ll1.insert_values([1,3,5])
ll2 = LinkedList(); ll2.insert_values([2,4,6])
merged_head = merge_two_sorted_lists(ll1.head, ll2.head)
merged = LinkedList(); merged.head = merged_head
merged.print()  # Output: 1 --> 2 --> 3 --> 4 --> 5 --> 6
