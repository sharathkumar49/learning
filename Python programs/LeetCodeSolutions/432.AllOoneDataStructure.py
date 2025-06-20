"""
432. All O`one Data Structure

Design a data structure to support the following operations:
- Inc(Key): Inserts a new key with value 1. Or increments an existing key by 1.
- Dec(Key): Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
- GetMaxKey(): Returns one of the keys with maximal value. If no element exists, return an empty string "".
- GetMinKey(): Returns one of the keys with minimal value. If no element exists, return an empty string "".

Constraints:
- All keys are non-empty strings consisting of lowercase English letters.
- The number of operations will not exceed 10^5.
- The total number of keys will not exceed 10^5.

Example:
Input: ["AllOne","inc","inc","getMaxKey","getMinKey","inc","getMaxKey","getMinKey"]
       [[],["hello"],["hello"],[],[],["leet"],[],[]]
Output: [null,null,null,"hello","hello",null,"hello","leet"]
"""

class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = self.next = None

class AllOne:
    def __init__(self):
        self.head = Node(float('-inf'))
        self.tail = Node(float('inf'))
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key2node = {}

    def _add_node(self, prev, node):
        node.next = prev.next
        node.prev = prev
        prev.next.prev = node
        prev.next = node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key: str) -> None:
        if key in self.key2node:
            node = self.key2node[key]
            nxt = node.next
            if nxt == self.tail or nxt.count > node.count + 1:
                new = Node(node.count + 1)
                self._add_node(node, new)
            else:
                new = nxt
            new.keys.add(key)
            self.key2node[key] = new
            node.keys.remove(key)
            if not node.keys:
                self._remove_node(node)
        else:
            nxt = self.head.next
            if nxt == self.tail or nxt.count > 1:
                new = Node(1)
                self._add_node(self.head, new)
            else:
                new = nxt
            new.keys.add(key)
            self.key2node[key] = new

    def dec(self, key: str) -> None:
        if key not in self.key2node:
            return
        node = self.key2node[key]
        if node.count == 1:
            node.keys.remove(key)
            del self.key2node[key]
            if not node.keys:
                self._remove_node(node)
        else:
            prev = node.prev
            if prev == self.head or prev.count < node.count - 1:
                new = Node(node.count - 1)
                self._add_node(prev, new)
            else:
                new = prev
            new.keys.add(key)
            self.key2node[key] = new
            node.keys.remove(key)
            if not node.keys:
                self._remove_node(node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))

# Example usage:
obj = AllOne()
obj.inc("hello")
obj.inc("hello")
print(obj.getMaxKey())  # Output: "hello"
print(obj.getMinKey())  # Output: "hello"
obj.inc("leet")
print(obj.getMaxKey())  # Output: "hello"
print(obj.getMinKey())  # Output: "leet"
