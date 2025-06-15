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

def min_add_to_make_valid(s):
    stack = Stack()
    additions = 0
    for ch in s:
        if ch == '(': 
            stack.push(ch)
        else:
            if stack.is_empty():
                additions += 1
            else:
                stack.pop()
    return additions + stack.size()

# Example usage
if __name__ == "__main__":
    print(min_add_to_make_valid("())"))  # 1
    print(min_add_to_make_valid("((("))  # 3
    print(min_add_to_make_valid("()"))   # 0
