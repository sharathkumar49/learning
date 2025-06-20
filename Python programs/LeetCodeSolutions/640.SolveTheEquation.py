"""
640. Solve the Equation
Difficulty: Medium

Solve the equation given in the form of a string and return "x=#value". The equation contains only '+', '-', '=', 'x', and digits.

Example 1:
Input: equation = "x+5-3+x=6+x-2"
Output: "x=2"

Example 2:
Input: equation = "x=x"
Output: "Infinite solutions"

Constraints:
The equation contains only valid characters.
"""

def solveEquation(equation):
    left, right = equation.split('=')
    def parse(expr):
        expr = expr.replace('-', '+-')
        tokens = expr.split('+')
        x, num = 0, 0
        for t in tokens:
            if not t:
                continue
            if 'x' in t:
                coef = t.replace('x', '')
                if coef == '' or coef == '+':
                    x += 1
                elif coef == '-':
                    x -= 1
                else:
                    x += int(coef)
            else:
                num += int(t)
        return x, num
    x1, n1 = parse(left)
    x2, n2 = parse(right)
    if x1 == x2:
        return "Infinite solutions" if n1 == n2 else "No solution"
    return f"x={(n2-n1)//(x1-x2)}"

# Example usage
if __name__ == "__main__":
    print(solveEquation("x+5-3+x=6+x-2"))  # Output: "x=2"
    print(solveEquation("x=x"))            # Output: "Infinite solutions"
