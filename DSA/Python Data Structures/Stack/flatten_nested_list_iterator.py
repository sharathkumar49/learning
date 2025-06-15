from collections import deque
from collections.abc import Iterator

class Stack:
    def __init__(self):
        self.container = deque()
    def push(self, val):
        self.container.append(val)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container) == 0
    def size(self):
        return len(self.container)

class NestedIterator:
    def __init__(self, nestedList):
        self.stack = Stack()
        self._push_list(nestedList)
    def _push_list(self, lst):
        for item in reversed(lst):
            self.stack.push(item)
    def next(self):
        return self.stack.pop()
    def hasNext(self):
        while not self.stack.is_empty():
            top = self.stack.peek()
            if isinstance(top, int):
                return True
            self.stack.pop()
            self._push_list(top)
        return False

# Example usage
if __name__ == "__main__":
    nestedList = [1, [4, [6]]]
    i = NestedIterator(nestedList)
    result = []
    while i.hasNext():
        result.append(i.next())
    print(result)  # [1, 4, 6]
