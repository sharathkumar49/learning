# Problem: Implement a stack that supports push, pop, top, and 
# retrieving the minimum element in O(1) time.


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        return self.stack[-1] if self.stack else None

    def get_min(self):
        return self.min_stack[-1] if self.min_stack else None

# Test Cases
s = MinStack()
s.push(5)
s.push(3)
s.push(7)
print(s.get_min())  # 3
s.pop()
print(s.get_min())  # 3

# Time Complexity: O(1) for push, pop, top, and get_min operations.




# Problem:
# You need to implement a stack that, in addition to 
# standard stack operations (push, pop, top), can also 
# return the minimum element in constant O(1) time.

# Implementation:

# Class: MinStack

# - Attributes:
#   - 'self.stack': The main stack that stores all values.
#   - 'self.min_stack': An auxiliary stack that keeps track of the minimum values.

# Methods

# - '__init__(self)'
#   - Initializes both 'stack' and 'min_stack' as empty lists.

# - 'push(self, val)'
#   - Adds 'val' to the main stack.
#   - If 'min_stack' is empty or 'val' is less than or equal to the current minimum (top of 'min_stack'), it also pushes 'val' onto 'min_stack'.
#   - This ensures the top of 'min_stack' always holds the minimum value so far.

# - 'pop(self)'
#   - Removes the top element from the main stack.
#   - If the popped value is equal to the top of 'min_stack', it also pops from 'min_stack'.
#   - This keeps 'min_stack' in sync with the main stack regarding minimum values.

# - 'top(self)'
#   - Returns the top element of the main stack, or 'None' if the stack is empty.

# - 'get_min(self)'
#   - Returns the top element of 'min_stack' (the current minimum), or 'None' if 'min_stack' is empty.


# Test Cases:

# s = MinStack()
# s.push(5)
# s.push(3)
# s.push(7)
# print(s.get_min())  # 3
# s.pop()
# print(s.get_min())  # 3

# - Pushes 5, 3, and 7 onto the stack.
# - The minimum after pushing 5 and 3 is 3.
# - After pushing 7, the minimum remains 3.
# - After popping 7, the minimum is still 3.


# Summary:  
# This program efficiently maintains the minimum value in a stack at all times using an auxiliary stack, allowing constant-time retrieval of the minimum element.