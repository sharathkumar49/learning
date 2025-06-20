"""
LeetCode 736. Parse Lisp Expression

You are given a string expression representing a Lisp-like expression to evaluate.

Return the result of evaluating the expression.

Example 1:
Input: expression = "(add 1 2)"
Output: 3

Example 2:
Input: expression = "(mult 3 (add 2 3))"
Output: 15

Example 3:
Input: expression = "(let x 2 (mult x 5))"
Output: 10

Constraints:
- 1 <= expression.length <= 2000
- The expression is well-formed with no leading or trailing spaces.
- The expression only contains 'let', 'add', 'mult', integers, and variable names.
"""
def evaluate(expression: str) -> int:
    def parse(tokens):
        token = tokens.pop(0)
        if token == '(':  # start of expression
            op = tokens.pop(0)
            if op == 'let':
                env.append(env[-1].copy())
                while tokens[0] != ')':
                    if len(tokens) > 2 and tokens[1] != ')':
                        var = tokens.pop(0)
                        val = parse(tokens)
                        env[-1][var] = val
                    else:
                        val = parse(tokens)
                        env.pop()
                        tokens.pop(0)  # remove ')'
                        return val
            elif op == 'add':
                v1 = parse(tokens)
                v2 = parse(tokens)
                tokens.pop(0)  # remove ')'
                return v1 + v2
            elif op == 'mult':
                v1 = parse(tokens)
                v2 = parse(tokens)
                tokens.pop(0)  # remove ')'
                return v1 * v2
        elif token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            return int(token)
        else:
            for scope in reversed(env):
                if token in scope:
                    return scope[token]
    def tokenize(expr):
        expr = expr.replace('(', ' ( ').replace(')', ' ) ')
        return expr.split()
    env = [{}]
    tokens = tokenize(expression)
    return parse(tokens)

# Example usage
if __name__ == "__main__":
    print(evaluate("(add 1 2)"))  # Output: 3
    print(evaluate("(mult 3 (add 2 3))"))  # Output: 15
    print(evaluate("(let x 2 (mult x 5))"))  # Output: 10
