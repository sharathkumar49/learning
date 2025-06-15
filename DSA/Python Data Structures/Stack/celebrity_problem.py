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


# Problem: Find the celebrity (if any) in a party of n people. 
# Celebrity Definition: Everyone knows the celebrity, but the
# celebrity knows no one.


def find_celebrity(matrix):
    n = len(matrix)
    stack = Stack()
    for i in range(n):
        stack.push(i)
    print("Initial stack:", list(stack.container))

    while stack.size() > 1:
        a = stack.pop()
        print("Popped a:", a)
        b = stack.pop()
        print("Popped b:", b)
        print("Comparing a and b:", a, b)
        if matrix[a][b]:
            print(matrix[a][b], "means a knows b")
            stack.push(b)  # a knows b, a is not celebrity
        else:
            print(matrix[a][b], "means a doesn't know b")
            stack.push(a)  # a doesn't know b, b is not celebrity

    candidate = stack.pop()
    if all(matrix[i][candidate] for i in range(n) if i != candidate) and \
       all(not matrix[candidate][i] for i in range(n)):
        return candidate
    return -1

# Example Party Matrix
party = [[0, 1, 1],
         [0, 0, 1],
         [0, 0, 0]]
print(find_celebrity(party))  # 2
