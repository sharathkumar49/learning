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

def trap(height):
    stack = Stack()
    water = 0
    i = 0
    n = len(height)
    while i < n:
        while not stack.is_empty() and height[i] > height[stack.peek()]:
            top = stack.pop()
            if stack.is_empty():
                break
            distance = i - stack.peek() - 1
            bounded_height = min(height[i], height[stack.peek()]) - height[top]
            water += distance * bounded_height
        stack.push(i)
        i += 1
    return water

# Example usage
if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(trap(height))  # 6
