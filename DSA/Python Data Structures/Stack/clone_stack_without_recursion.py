from collections import deque

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

def clone_stack(original):
    temp = Stack()
    clone = Stack()
    # Reverse original into temp
    while not original.is_empty():
        temp.push(original.pop())
    # Restore original and build clone
    while not temp.is_empty():
        val = temp.pop()
        original.push(val)
        clone.push(val)
    return clone

# Example usage
if __name__ == "__main__":
    s = Stack()
    for i in [1,2,3,4]:
        s.push(i)
    c = clone_stack(s)
    print(list(s.container))  # [1,2,3,4]
    print(list(c.container))  # [1,2,3,4]
