# Reverse Nodes in Groups of Increasing Size
from linked_list_impl import Node, LinkedList

def reverse_increasing_groups(head):
    k = 1
    curr = head
    prev_tail = None
    new_head = None
    while curr:
        count = 0
        group_head = curr
        prev = None
        temp = curr
        # Check if enough nodes
        for _ in range(k):
            if not temp:
                break
            temp = temp.next
            count += 1
        if count < k:
            if prev_tail:
                prev_tail.next = curr
            break
        # Reverse k nodes
        count = 0
        while curr and count < k:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            count += 1
        if not new_head:
            new_head = prev
        if prev_tail:
            prev_tail.next = prev
        prev_tail = group_head
        k += 1
    return new_head if new_head else head

# Example usage:
ll = LinkedList(); ll.insert_values([1,2,3,4,5,6,7,8,9])
ll.head = reverse_increasing_groups(ll.head)
ll.print()  # Output: 1 --> 2 --> 3 --> 4 --> 5 --> 6 --> 7 --> 8 --> 9 (with groups reversed)
