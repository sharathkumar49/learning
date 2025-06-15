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

def daily_temperatures(temperatures):
    n = len(temperatures)
    answer = [0] * n
    stack = Stack()
    for i in range(n-1, -1, -1):
        while not stack.is_empty() and temperatures[stack.peek()] <= temperatures[i]:
            stack.pop()
        if not stack.is_empty():
            answer[i] = stack.peek() - i
        stack.push(i)
    return answer

# Example usage
if __name__ == "__main__":
    temps = [73, 74, 75, 71, 69, 72, 76, 73]
    print(daily_temperatures(temps))  # [1, 1, 4, 2, 1, 1, 0, 0]
