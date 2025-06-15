# Clone a Linked List with Next and Random Pointers
class RandomNode:
    def __init__(self, data=None, next=None, random=None):
        self.data = data
        self.next = next
        self.random = random

def clone_list(head):
    if not head:
        return None
    # Step 1: Insert cloned nodes
    curr = head
    while curr:
        new_node = RandomNode(curr.data, curr.next)
        curr.next = new_node
        curr = new_node.next
    # Step 2: Set random pointers
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next
    # Step 3: Separate lists
    curr = head
    clone_head = head.next
    while curr:
        clone = curr.next
        curr.next = clone.next
        clone.next = clone.next.next if clone.next else None
        curr = curr.next
    return clone_head
# Example usage omitted for brevity
