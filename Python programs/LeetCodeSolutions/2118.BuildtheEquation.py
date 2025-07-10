"""
LeetCode 2118. Build the Equation

Given a string equation, return the solution to the equation.

Example:
Input: equation = "x+5-3+x=6+x-2"
Output: "x=2"

Constraints:
- equation contains only '+', '-', '=', 'x', and digits.
"""

def solveEquation(equation):
    left, right = equation.split('=')
    def parse(expr):
        x = num = 0
        sign = 1
        i = 0
        while i < len(expr):
            if expr[i] == '+':
                sign = 1
                i += 1
            elif expr[i] == '-':
                sign = -1
                i += 1
            else:
                j = i
                while j < len(expr) and expr[j].isdigit():
                    j += 1
                if j < len(expr) and expr[j] == 'x':
                    val = int(expr[i:j]) if j > i else 1
                    x += sign * val
                    j += 1
                else:
                    val = int(expr[i:j])
                    num += sign * val
                i = j
        return x, num
    x1, n1 = parse(left)
    x2, n2 = parse(right)
    if x1 == x2:
        return "No solution" if n1 != n2 else "Infinite solutions"
    return f"x={(n2-n1)//(x1-x2)}"

# Example usage:
# print(solveEquation("x+5-3+x=6+x-2"))  # Output: "x=2"
