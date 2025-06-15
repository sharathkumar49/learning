# Remove All Duplicates from Sorted List but Keep One Occurrence
from linked_list_impl import Node, LinkedList

def remove_duplicates_from_sorted_list_keep_one(head):
    curr = head
    while curr and curr.next:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head

# Example usage:
ll = LinkedList(); ll.insert_values([1,1,2,3,3,3,4,5,5])
ll.head = remove_duplicates_from_sorted_list_keep_one(ll.head)
ll.print()  # Output: 1 --> 2 --> 3 --> 4 --> 5
