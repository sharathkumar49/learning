# Flatten a Linked List Where Each Node Has a Next and a Down Pointer
class DownNode:
    def __init__(self, data=None, next=None, down=None):
        self.data = data
        self.next = next
        self.down = down

def merge(a, b):
    if not a: return b
    if not b: return a
    if a.data < b.data:
        a.down = merge(a.down, b)
        return a
    else:
        b.down = merge(a, b.down)
        return b

def flatten(head):
    if not head or not head.next:
        return head
    head.next = flatten(head.next)
    head = merge(head, head.next)
    return head
# Example usage omitted for brevity
