# Copy List with Random Pointer
# Each node has an extra random pointer. Return a deep copy of the list.
# LeetCode 138
class RandomListNode:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def copy_random_list(head):
    if not head:
        return None
    # Step 1: Interleave copied nodes
    curr = head
    while curr:
        new_node = RandomListNode(curr.val, curr.next)
        curr.next = new_node
        curr = new_node.next
    # Step 2: Assign random pointers
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next
    # Step 3: Separate the lists
    curr = head
    copy_head = head.next
    while curr:
        copy = curr.next
        curr.next = copy.next
        copy.next = copy.next.next if copy.next else None
        curr = curr.next
    return copy_head
# Example usage omitted for brevity
