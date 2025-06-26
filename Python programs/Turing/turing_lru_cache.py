# Turing: LRU Cache
# Design and implement a data structure for Least Recently Used (LRU) cache.
class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.size = 0
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    def _remove_node(self, node):
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev
    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)
    def _pop_tail(self):
        res = self.tail.prev
        self._remove_node(res)
        return res
    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node:
            return -1
        self._move_to_head(node)
        return node.value
    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if not node:
            newNode = DLinkedNode(key, value)
            self.cache[key] = newNode
            self._add_node(newNode)
            self.size += 1
            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.value = value
            self._move_to_head(node)

# Example usage and test cases can be added as needed.
