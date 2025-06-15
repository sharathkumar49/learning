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

def calculate_span(prices):
    n = len(prices)
    stack = Stack()
    span = [0] * n
    for i in range(n):
        while not stack.is_empty() and prices[stack.peek()] <= prices[i]:
            stack.pop()
        span[i] = i + 1 if stack.is_empty() else i - stack.peek()
        stack.push(i)
    return span

# Example usage
if __name__ == "__main__":
    prices = [100, 80, 60, 70, 60, 75, 85]
    print(calculate_span(prices))  # [1, 1, 1, 2, 1, 4, 6]
