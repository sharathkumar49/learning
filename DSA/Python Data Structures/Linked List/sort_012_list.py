# Sort a Linked List of 0s, 1s, and 2s
from linked_list_impl import Node, LinkedList

def sort_012_list(head):
    count = [0, 0, 0]
    curr = head
    while curr:
        count[curr.data] += 1
        curr = curr.next
    curr = head
    i = 0
    while curr:
        if count[i] == 0:
            i += 1
        else:
            curr.data = i
            count[i] -= 1
            curr = curr.next
    return head

# Example usage:
ll = LinkedList(); ll.insert_values([1,2,0,1,2,0,1,2])
ll.head = sort_012_list(ll.head)
ll.print()  # Output: 0 --> 0 --> 1 --> 1 --> 1 --> 2 --> 2 --> 2
