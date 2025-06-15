# Remove All Duplicates from Sorted List (No Duplicates Left)
from linked_list_impl import Node, LinkedList

def remove_duplicates_from_sorted_list_all(head):
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    curr = head
    while curr:
        duplicate = False
        while curr.next and curr.data == curr.next.data:
            curr = curr.next
            duplicate = True
        if duplicate:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    return dummy.next

# Example usage:
ll = LinkedList(); ll.insert_values([1,1,2,3,3,3,4,5,5])
ll.head = remove_duplicates_from_sorted_list_all(ll.head)
ll.print()  # Output: 2 --> 4
