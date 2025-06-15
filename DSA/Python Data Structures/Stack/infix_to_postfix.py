from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1] if self.container else None

    def is_empty(self):
        return len(self.container) == 0

# Define precedence and associativity for operators
PRECEDENCE = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
ASSOCIATIVITY = {'+': 'L', '-': 'L', '*': 'L', '/': 'L', '^': 'R'}

def is_higher_precedence(op1, op2):
    """Returns True if op1 has higher precedence than op2."""
    return PRECEDENCE[op1] > PRECEDENCE[op2]

def is_same_precedence_left_associative(op1, op2):
    """Checks if both operators have same precedence and left associativity."""
    return PRECEDENCE[op1] == PRECEDENCE[op2] and ASSOCIATIVITY[op1] == 'L'

def infix_to_postfix(expression):
    stack = Stack()
    output = []

    for char in expression:
        if char.isalnum():  # If operand, append to output
            output.append(char)
        elif char in PRECEDENCE:  # If operator, process stack precedence
            while (not stack.is_empty() and stack.peek() != '(' and
                   (is_higher_precedence(stack.peek(), char) or is_same_precedence_left_associative(stack.peek(), char))):
                output.append(stack.pop())
            stack.push(char)
        elif char == '(':  # Push left parenthesis
            stack.push(char)
        elif char == ')':  # Pop until left parenthesis is found
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()  # Remove '('

    # Pop remaining operators
    while not stack.is_empty():
        output.append(stack.pop())

    return ''.join(output)

# Example usage
expression = "A+B*(C^D-E)"
postfix = infix_to_postfix(expression)
print("Postfix Expression:", postfix)
