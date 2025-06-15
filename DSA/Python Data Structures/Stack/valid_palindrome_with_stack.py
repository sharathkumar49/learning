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

def is_palindrome(s):
    stack = Stack()
    for ch in s:
        stack.push(ch)
    reversed_s = ''
    while not stack.is_empty():
        reversed_s += stack.pop()
    return s == reversed_s

# Example usage
if __name__ == "__main__":
    print(is_palindrome("racecar"))  # True
    print(is_palindrome("hello"))    # False
