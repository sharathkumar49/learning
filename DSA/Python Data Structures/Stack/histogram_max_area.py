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

def largest_rectangle_area(heights):
    stack = Stack()
    max_area = 0
    index = 0
    n = len(heights)
    while index < n:
        if stack.is_empty() or heights[index] >= heights[stack.peek()]:
            stack.push(index)
            index += 1
        else:
            top = stack.pop()
            width = index if stack.is_empty() else index - stack.peek() - 1
            max_area = max(max_area, heights[top] * width)
    while not stack.is_empty():
        top = stack.pop()
        width = index if stack.is_empty() else index - stack.peek() - 1
        max_area = max(max_area, heights[top] * width)
    return max_area

# Example usage
if __name__ == "__main__":
    heights = [2,1,5,6,2,3]
    print(largest_rectangle_area(heights))  # 10
