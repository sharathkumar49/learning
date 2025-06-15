# Problem: Evaluate a mathematical expression given in postfix notation.

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


def eval_rpn(tokens):
    stack = Stack()  # Use the custom Stack class

    for token in tokens:
        if token in "+-*/":
            b, a = stack.pop(), stack.pop()
            stack.push(str(int(eval(a + token + b))))
        else:
            stack.push(token)  # Push operand onto stack

    return int(stack.pop())  # Final result

# Test Cases
print(eval_rpn(["2", "1", "+", "3", "*"]))  # Output: 9
print(eval_rpn(["4", "13", "5", "/", "+"]))  # Output: 6







# Using list as a stack
def eval_rpn(tokens):
    stack = []
    for token in tokens:
        if token in "+-*/":
            b, a = stack.pop(), stack.pop()
            stack.append(str(int(eval(a + token + b))))
        else:
            stack.append(token)
    return int(stack.pop())

# Test Cases
print(eval_rpn(["2", "1", "+", "3", "*"]))  # 9
print(eval_rpn(["4", "13", "5", "/", "+"]))  # 6


# Time Complexity: O(n)

# Problem:
# Evaluate a mathematical expression given in postfix (Reverse Polish) notation,
# where operators follow their operands.

# How the Program Works:
# - Function: 'eval_rpn(tokens)'
# - 'tokens' is a list of strings, each string is either an integer or an operator ('+', '-', '*', '/').

# Steps:
# 1. Initialize a stack:  
#    'stack = []' is used to store operands.

# 2. Iterate through each token:
#    - If the token is an operator ('+', '-', '*', '/'):
#      - Pop the top two elements from the stack ('b' and 'a').
#      - Evaluate the expression 'a operator b' using Python’s 'eval' function.
#      - Convert the result to integer and string, then push it back onto the stack.
#    - If the token is a number:
#      - Push it onto the stack.

# 3. Return the result:
#    - After processing all tokens, the stack will have one element,
# which is the result. Convert it to integer and return.



# Example:
# - For '["2", "1", "+", "3", "*"]':
#   - 2 and 1 are pushed.
#   - '+' pops 2 and 1, computes 2+1=3, pushes 3.
#   - 3 is pushed.
#   - '*' pops 3 and 3, computes 3*3=9, pushes 9.
#   - Returns 9.

# - For '["4", "13", "5", "/", "+"]':
#   - 4, 13, 5 are pushed.
#   - '/' pops 13 and 5, computes 13/5=2, pushes 2.
#   - '+' pops 4 and 2, computes 4+2=6, pushes 6.
#   - Returns 6.



# Summary
# This program uses a stack to evaluate postfix expressions efficiently.
# It processes each token, applies operators to the topmost operands, 
# and always leaves the final result at the top of the stack.