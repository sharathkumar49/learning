# Check if a linked list has a cycle
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

if __name__ == "__main__":
    # Example usage
    a = Node(1)
    b = Node(2)
    c = Node(3)
    a.next = b
    b.next = c
    # Uncomment next line to create a cycle
    # c.next = a
    print("Cycle detected!" if has_cycle(a) else "No cycle.")
