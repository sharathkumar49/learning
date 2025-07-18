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

def remove_adjacent_duplicates(s):
    stack = Stack()
    for ch in s:
        if not stack.is_empty() and stack.peek() == ch:
            stack.pop()
        else:
            stack.push(ch)
    return ''.join(stack.container)

# Example usage
if __name__ == "__main__":
    print(remove_adjacent_duplicates("abbaca"))  # ca
    print(remove_adjacent_duplicates("azxxzy"))  # ay
