"""
227. Basic Calculator II
https://leetcode.com/problems/basic-calculator-ii/

Given a string s which represents an expression, evaluate this expression and return its value. The integer division should truncate toward zero.

Constraints:
- 1 <= s.length <= 3 * 10^5
- s consists of non-negative integers, '+', '-', '*', '/', and ' '.
- s represents a valid expression.
- All the integers in the expression are non-negative integers in the range [0, 2^31 - 1].
- The answer is guaranteed to fit in a 32-bit integer.

Example 1:
Input: s = "3+2*2"
Output: 7

Example 2:
Input: s = " 3/2 "
Output: 1

Example 3:
Input: s = " 3+5 / 2 "
Output: 5
"""
def calculate(s):
    stack = []
    num = 0
    sign = '+'
    s += '+'
    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c in '+-*/':
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack[-1] *= num
            elif sign == '/':
                stack[-1] = int(stack[-1] / num)
            sign = c
            num = 0
    return sum(stack)

# Example usage:
if __name__ == "__main__":
    print(calculate("3+2*2"))      # Output: 7
    print(calculate(" 3/2 "))     # Output: 1
    print(calculate(" 3+5 / 2 ")) # Output: 5
