# Flatten a Multilevel Linked List
# Each node may have a child pointer to another linked list. Flatten the list so all nodes appear in a single-level, depth-first order.
class MultiNode:
    def __init__(self, data=None, next=None, child=None):
        self.data = data
        self.next = next
        self.child = child

def flatten(head):
    if not head:
        return None
    stack = []
    curr = head
    while curr:
        if curr.child:
            if curr.next:
                stack.append(curr.next)
            curr.next = curr.child
            curr.child = None
        if not curr.next and stack:
            curr.next = stack.pop()
        curr = curr.next
    return head
# Example usage omitted for brevity
