# Insert a Node in a Sorted Linked List
from linked_list_impl import Node, LinkedList

def insert_in_sorted_list(head, value):
    new_node = Node(value)
    if not head or value < head.data:
        new_node.next = head
        return new_node
    curr = head
    while curr.next and curr.next.data < value:
        curr = curr.next
    new_node.next = curr.next
    curr.next = new_node
    return head

# Example usage:
ll = LinkedList(); ll.insert_values([1,3,5,7,9])
ll.head = insert_in_sorted_list(ll.head, 6)
ll.print()  # Output: 1 --> 3 --> 5 --> 6 --> 7 --> 9
