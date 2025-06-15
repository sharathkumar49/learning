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

def remove_k_digits(num, k):
    stack = Stack()
    for digit in num:
        while k > 0 and not stack.is_empty() and stack.peek() > digit:
            stack.pop()
            k -= 1
        stack.push(digit)
    # Remove remaining digits from the end if k > 0
    while k > 0:
        stack.pop()
        k -= 1
    result = ''.join(stack.container).lstrip('0')
    return result if result else '0'

# Example usage
if __name__ == "__main__":
    print(remove_k_digits("1432219", 3))  # "1219"
    print(remove_k_digits("10200", 1))   # "200"
    print(remove_k_digits("10", 2))      # "0"
