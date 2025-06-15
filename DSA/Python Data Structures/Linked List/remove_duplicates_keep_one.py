# Remove All Duplicates but Keep One Occurrence
# Remove duplicates from an unsorted linked list, keeping only the first occurrence of each value.
from linked_list_impl import Node, LinkedList

def remove_duplicates_keep_one(head):
    seen = set()
    prev = None
    curr = head
    while curr:
        if curr.data in seen:
            prev.next = curr.next
        else:
            seen.add(curr.data)
            prev = curr
        curr = curr.next
    return head

# Example usage:
ll = LinkedList(); ll.insert_values([1,2,3,2,4,1,5,3])
ll.head = remove_duplicates_keep_one(ll.head)
ll.print()  # Output: 1 --> 2 --> 3 --> 4 --> 5
