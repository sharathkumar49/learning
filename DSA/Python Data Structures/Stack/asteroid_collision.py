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

def asteroid_collision(asteroids):
    stack = Stack()
    for ast in asteroids:
        while not stack.is_empty() and ast < 0 < stack.peek():
            if stack.peek() < -ast:
                stack.pop()
                continue
            elif stack.peek() == -ast:
                stack.pop()
            break
        else:
            stack.push(ast)
    return list(stack.container)

# Example usage
if __name__ == "__main__":
    print(asteroid_collision([5, 10, -5]))        # [5, 10]
    print(asteroid_collision([8, -8]))            # []
    print(asteroid_collision([10, 2, -5]))        # [10]
    print(asteroid_collision([-2, -1, 1, 2]))     # [-2, -1, 1, 2]
