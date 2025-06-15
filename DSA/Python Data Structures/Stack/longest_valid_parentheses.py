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

def longest_valid_parentheses(s):
    stack = Stack()
    stack.push(-1)
    max_len = 0
    for i, ch in enumerate(s):
        if ch == '(': stack.push(i)
        else:
            stack.pop()
            if stack.is_empty():
                stack.push(i)
            else:
                max_len = max(max_len, i - stack.peek())
    return max_len

# Example usage
if __name__ == "__main__":
    print(longest_valid_parentheses("(()"))  # 2
    print(longest_valid_parentheses(")()())"))  # 4
    print(longest_valid_parentheses("") ) # 0
