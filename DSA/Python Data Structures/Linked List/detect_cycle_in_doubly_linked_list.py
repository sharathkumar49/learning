# Detect Cycle in a Doubly Linked List
class DNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_values(self, data_list):
        self.head = None
        prev = None
        for data in data_list:
            node = DNode(data)
            if prev:
                prev.next = node
                node.prev = prev
            else:
                self.head = node
            prev = node
        return prev

    def create_cycle(self, pos):
        last = self.head
        cycle_node = None
        idx = 0
        curr = self.head
        while curr:
            if idx == pos:
                cycle_node = curr
            last = curr
            curr = curr.next
            idx += 1
        if cycle_node:
            last.next = cycle_node
            cycle_node.prev = last

    def has_cycle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# Example usage:
dll = DoublyLinkedList()
dll.insert_values([1,2,3,4,5])
dll.create_cycle(1)
print('Cycle detected (doubly):', dll.has_cycle())  # Output: True
