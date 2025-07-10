"""
LeetCode 1597. Build Binary Expression Tree From Infix Expression

Given a string s representing an infix expression, build a binary expression tree and return its root. Each node is either an operator or an operand.

Example 1:
Input: s = "2-3/(5*2)+1"
Output: [+,2,-,/,3,*,5,2,1]

Constraints:
- 1 <= s.length <= 100
- s consists of digits and operators '+', '-', '*', '/'.
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(s):
    def precedence(op):
        if op in ('+', '-'): return 1
        if op in ('*', '/'): return 2
        return 0
    ops, nodes = [], []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            j = i
            while j < len(s) and s[j].isdigit():
                j += 1
            nodes.append(Node(s[i:j]))
            i = j
        elif s[i] == '(': 
            ops.append(s[i])
            i += 1
        elif s[i] == ')':
            while ops and ops[-1] != '(': 
                op = ops.pop()
                r = nodes.pop()
                l = nodes.pop()
                nodes.append(Node(op, l, r))
            ops.pop()
            i += 1
        else:
            while ops and precedence(ops[-1]) >= precedence(s[i]):
                op = ops.pop()
                r = nodes.pop()
                l = nodes.pop()
                nodes.append(Node(op, l, r))
            ops.append(s[i])
            i += 1
    while ops:
        op = ops.pop()
        r = nodes.pop()
        l = nodes.pop()
        nodes.append(Node(op, l, r))
    return nodes[-1]

# Example usage:
# s = "2-3/(5*2)+1"
# root = buildTree(s)
