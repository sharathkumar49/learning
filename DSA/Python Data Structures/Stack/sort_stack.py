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

def sort_stack(stack):
    if not stack.is_empty():
        temp = stack.pop()
        sort_stack(stack)
        insert_sorted(stack, temp)

def insert_sorted(stack, element):
    if stack.is_empty() or element > stack.peek():
        stack.push(element)
    else:
        temp = stack.pop()
        insert_sorted(stack, element)
        stack.push(temp)

# Example usage
if __name__ == "__main__":
    s = Stack()
    for x in [3, 1, 4, 2]:
        s.push(x)
    sort_stack(s)
    sorted_list = []
    while not s.is_empty():
        sorted_list.append(s.pop())
    print(sorted_list[::-1])  # [1, 2, 3, 4]
