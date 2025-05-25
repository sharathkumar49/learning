# Detect and remove loop in linked list
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def detect_and_remove_loop(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return False
    slow = head
    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next
    fast.next = None
    return True

if __name__ == "__main__":
    a = Node(1); b = Node(2); c = Node(3)
    a.next = b; b.next = c; c.next = b
    print(detect_and_remove_loop(a))
