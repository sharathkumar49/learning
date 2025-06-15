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

def maximal_rectangle(matrix):
    if not matrix or not matrix[0]:
        return 0
    n = len(matrix[0])
    heights = [0] * n
    max_area = 0
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
    for row in matrix:
        for i in range(n):
            heights[i] = heights[i] + 1 if row[i] == 1 else 0
        max_area = max(max_area, largest_rectangle_area(heights))
    return max_area

# Example usage
if __name__ == "__main__":
    matrix = [
        [1,0,1,0,0],
        [1,0,1,1,1],
        [1,1,1,1,1],
        [1,0,0,1,0]
    ]
    print(maximal_rectangle(matrix))  # 6
