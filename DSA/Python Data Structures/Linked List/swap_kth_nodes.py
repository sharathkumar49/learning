# Swap kth Node from Beginning with kth Node from End
from linked_list_impl import Node, LinkedList

def swap_kth_nodes(head, k):
    n = 0
    curr = head
    while curr:
        n += 1
        curr = curr.next
    if k > n:
        return head
    if 2*k - 1 == n:
        return head
    prevX = None
    currX = head
    for i in range(k-1):
        prevX = currX
        currX = currX.next
    prevY = None
    currY = head
    for i in range(n-k):
        prevY = currY
        currY = currY.next
    if prevX:
        prevX.next = currY
    if prevY:
        prevY.next = currX
    temp = currX.next
    currX.next = currY.next
    currY.next = temp
    if k == 1:
        head = currY
    if k == n:
        head = currX
    return head

# Example usage:
ll = LinkedList(); ll.insert_values([1,2,3,4,5,6,7,8,9])
ll.head = swap_kth_nodes(ll.head, 3)
ll.print()  # Output: 1 --> 2 --> 7 --> 4 --> 5 --> 6 --> 3 --> 8 --> 9
