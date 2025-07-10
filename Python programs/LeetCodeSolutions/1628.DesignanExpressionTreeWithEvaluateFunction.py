"""
LeetCode 1628. Design an Expression Tree With Evaluate Function

Given a postfix expression, build an expression tree and return its root. Each node is either an operator or an operand. Implement an evaluate() method to compute the value of the expression.

Example 1:
Input: s = ["3","4","+","2","*","7","/"]
Output: 2

Constraints:
- 1 <= s.length <= 100
- s consists of integers and operators '+', '-', '*', '/'.
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def evaluate(self):
        if self.val.isdigit() or (self.val[0] == '-' and self.val[1:].isdigit()):
            return int(self.val)
        l = self.left.evaluate()
        r = self.right.evaluate()
        if self.val == '+': return l + r
        if self.val == '-': return l - r
        if self.val == '*': return l * r
        if self.val == '/': return int(l / r)

class TreeBuilder(object):
    def buildTree(self, postfix):
        stack = []
        for token in postfix:
            if token in '+-*/':
                r = stack.pop()
                l = stack.pop()
                stack.append(Node(token, l, r))
            else:
                stack.append(Node(token))
        return stack[-1]

# Example usage:
# postfix = ["3","4","+","2","*","7","/"]
# obj = TreeBuilder()
# expTree = obj.buildTree(postfix)
# print(expTree.evaluate())  # Output: 2
