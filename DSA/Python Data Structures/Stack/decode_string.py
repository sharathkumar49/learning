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

def decode_string(s):
    stack = Stack()
    for char in s:
        if char != ']':
            stack.push(char)
        else:
            substr = ''
            while not stack.is_empty() and stack.peek() != '[':
                substr = stack.pop() + substr
            stack.pop()  # Remove '['
            k = ''
            while not stack.is_empty() and stack.peek().isdigit():
                k = stack.pop() + k
            stack.push(int(k) * substr)
    return ''.join(stack.container)

# Example usage
if __name__ == "__main__":
    print(decode_string("3[a2[c]]"))  # accaccacc
    print(decode_string("2[abc]3[cd]ef"))  # abcabccdcdcdef
