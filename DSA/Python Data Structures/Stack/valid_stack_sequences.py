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

def validate_stack_sequences(pushed, popped):
    stack = Stack()
    j = 0
    for x in pushed:
        stack.push(x)
        while not stack.is_empty() and j < len(popped) and stack.peek() == popped[j]:
            stack.pop()
            j += 1
    return stack.is_empty()

# Example usage
if __name__ == "__main__":
    print(validate_stack_sequences([1,2,3,4,5], [4,5,3,2,1]))  # True
    print(validate_stack_sequences([1,2,3,4,5], [4,3,5,1,2]))  # False
