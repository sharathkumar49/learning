# Remove Every k-th Node from the Linked List
from linked_list_impl import Node, LinkedList

def remove_every_kth_node(head, k):
    if k <= 1 or not head:
        return None
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    curr = head
    count = 1
    while curr:
        if count % k == 0:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
        count += 1
    return dummy.next

# Example usage:
ll = LinkedList(); ll.insert_values([1,2,3,4,5,6,7,8,9])
ll.head = remove_every_kth_node(ll.head, 4)
ll.print()  # Output: 1 --> 2 --> 3 --> 5 --> 6 --> 7 --> 9
