# Remove Alternate Nodes from a Linked List
from linked_list_impl import Node, LinkedList

def remove_alternate_nodes(head):
    curr = head
    while curr and curr.next:
        curr.next = curr.next.next
        curr = curr.next
    return head

# Example usage:
ll = LinkedList(); ll.insert_values([10, 20, 30, 40, 50, 60])
ll.head = remove_alternate_nodes(ll.head)
ll.print()  # Output: 10 --> 30 --> 50
