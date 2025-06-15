# Check if a Linked List is a Sublist of Another
from linked_list_impl import Node, LinkedList

def is_sublist(main_head, sub_head):
    if not sub_head:
        return True
    curr_main = main_head
    while curr_main:
        curr1, curr2 = curr_main, sub_head
        while curr1 and curr2 and curr1.data == curr2.data:
            curr1 = curr1.next
            curr2 = curr2.next
        if not curr2:
            return True
        curr_main = curr_main.next
    return False

# Example usage:
ll1 = LinkedList(); ll1.insert_values([1,2,3,4,5,6])
ll2 = LinkedList(); ll2.insert_values([3,4,5])
print('Is sublist:', is_sublist(ll1.head, ll2.head))  # Output: True
