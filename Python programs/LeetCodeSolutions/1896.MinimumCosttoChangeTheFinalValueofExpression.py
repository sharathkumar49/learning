"""
LeetCode 1896. Minimum Cost to Change the Final Value of Expression

Given a boolean expression with '1', '0', '&', '|', and parentheses, return the minimum number of operations to flip the final value.

Example:
Input: expression = "1&(0|1)"
Output: 1

Constraints:
- 1 <= expression.length <= 10^5
- expression consists of '1', '0', '&', '|', '(', ')'
"""

def minOperationsToFlip(expression):
    stack = []
    for c in expression:
        if c == '(': stack.append(c)
        elif c == ')':
            vals = []
            while stack[-1] != '(': vals.append(stack.pop())
            stack.pop()
            stack.append(vals[::-1])
        elif c in '01|&': stack.append(c)
    def eval_expr(expr):
        if isinstance(expr, str):
            if expr == '1': return (1, 1)
            if expr == '0': return (0, 1)
        if isinstance(expr, list):
            left, op, right = expr
            lval, lflip = eval_expr(left)
            rval, rflip = eval_expr(right)
            if op == '&':
                val = lval & rval
                flip = min(lflip, rflip) if val else (1 if lval or rval else min(lflip, rflip))
            else:
                val = lval | rval
                flip = min(lflip, rflip) if not val else (1 if not lval or not rval else min(lflip, rflip))
            return (val, flip)
    return eval_expr(stack[0])[1]

# Example usage:
# print(minOperationsToFlip("1&(0|1)"))  # Output: 1
