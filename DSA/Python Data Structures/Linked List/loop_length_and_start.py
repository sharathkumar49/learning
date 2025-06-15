# Find the Loop Length and Start Node in a Linked List
from linked_list_impl import Node, LinkedList

def loop_length_and_start(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # Find start
            slow2 = head
            while slow2 != slow:
                slow2 = slow2.next
                slow = slow.next
            # Find length
            count = 1
            temp = slow.next
            while temp != slow:
                temp = temp.next
                count += 1
            return (count, slow)
    return (0, None)

# Example usage:
ll = LinkedList(); ll.insert_values([1,2,3,4,5,6])
ll.create_cycle(2)
length, start = loop_length_and_start(ll.head)
print('Loop length:', length, 'Start node:', start.data if start else None)  # Output: 4, 3
