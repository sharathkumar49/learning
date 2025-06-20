"""
1106. Parsing A Boolean Expression

Given a string expression representing a boolean expression, return the result of evaluating it.

Constraints:
- 1 <= expression.length <= 20000
- expression consists of 't', 'f', '!', '&', '|', '(', ')', and ','

Example:
Input: expression = "!(f)"
Output: true
"""
def parseBoolExpr(expression: str) -> bool:
    def eval_expr(expr):
        if expr == 't': return True
        if expr == 'f': return False
        if expr[0] == '!':
            return not eval_expr(expr[2:-1])
        if expr[0] == '&':
            parts = split_args(expr[2:-1])
            return all(eval_expr(p) for p in parts)
        if expr[0] == '|':
            parts = split_args(expr[2:-1])
            return any(eval_expr(p) for p in parts)
    def split_args(s):
        args, bal, last = [], 0, 0
        for i, c in enumerate(s):
            if c == ',' and bal == 0:
                args.append(s[last:i])
                last = i+1
            elif c == '(': bal += 1
            elif c == ')': bal -= 1
        args.append(s[last:])
        return args
    return eval_expr(expression)

# Example usage:
expression = "!(f)"
print(parseBoolExpr(expression))  # Output: True
