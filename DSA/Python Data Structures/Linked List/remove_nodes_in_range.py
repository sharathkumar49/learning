# Remove Nodes with Values in a Given Range [low, high]
from linked_list_impl import Node, LinkedList

def remove_nodes_in_range(head, low, high):
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    curr = head
    while curr:
        if low <= curr.data <= high:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    return dummy.next

# Example usage:
ll = LinkedList(); ll.insert_values([1,5,10,15,20,25,30])
ll.head = remove_nodes_in_range(ll.head, 10, 20)
ll.print()  # Output: 1 --> 5 --> 25 --> 30
