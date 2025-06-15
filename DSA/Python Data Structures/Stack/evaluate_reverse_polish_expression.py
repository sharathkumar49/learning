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

def evaluate_reverse_polish_expression(tokens):
    stack = Stack()
    for token in tokens:
        if token in '+-*/':
            b = int(stack.pop())
            a = int(stack.pop())
            if token == '+':
                stack.push(a + b)
            elif token == '-':
                stack.push(a - b)
            elif token == '*':
                stack.push(a * b)
            elif token == '/':
                stack.push(int(a / b))
        else:
            stack.push(int(token))
    return stack.pop()

# Example usage
if __name__ == "__main__":
    print(evaluate_reverse_polish_expression(["2", "1", "+", "3", "*"]))  # 9
    print(evaluate_reverse_polish_expression(["4", "13", "5", "/", "+"]))  # 6
