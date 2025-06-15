from collections import deque
import re

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

def is_valid_html(xml):
    tag_pattern = re.compile(r'<(/?)(\w+)[^>]*>')
    stack = Stack()
    for match in tag_pattern.finditer(xml):
        closing, tag = match.groups()
        if not closing:
            stack.push(tag)
        else:
            if stack.is_empty() or stack.pop() != tag:
                return False
    return stack.is_empty()

# Example usage
if __name__ == "__main__":
    print(is_valid_html("<a><b></b></a>"))  # True
    print(is_valid_html("<a><b></a></b>"))  # False
    print(is_valid_html("<div><p></p></div>"))  # True
