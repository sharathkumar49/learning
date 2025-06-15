# Delete Every k-th Node in a Linked List
from linked_list_impl import Node, LinkedList

def delete_every_kth_node(head, k):
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
ll.head = delete_every_kth_node(ll.head, 3)
ll.print()  # Output: 1 --> 2 --> 4 --> 5 --> 7 --> 8
