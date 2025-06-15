# Check if Linked List is a Palindrome (O(1) space)
from linked_list_impl import Node, LinkedList

def is_palindrome(head):
    if not head or not head.next:
        return True
    # Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # Reverse second half
    prev = None
    curr = slow
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    # Compare halves
    first, second = head, prev
    result = True
    while second:
        if first.data != second.data:
            result = False
            break
        first = first.next
        second = second.next
    # (Optional) Restore the list
    return result

# Example usage:
ll = LinkedList()
ll.insert_values([1,2,3,2,1])
print('Is palindrome:', is_palindrome(ll.head))  # Output: True
