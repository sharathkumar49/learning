"""
224. Basic Calculator
https://leetcode.com/problems/basic-calculator/

Given a string s representing a valid expression, implement a basic calculator to evaluate it, supporting '+', '-', '(', ')', and non-negative integers.

Constraints:
- 1 <= s.length <= 3 * 10^5
- s consists of digits, '+', '-', '(', ')', and ' '.
- s represents a valid expression.
- '+' is not used as a unary operation.
- '-' could be used as a unary operation but it is guaranteed that the expression is valid.

Example 1:
Input: s = "1 + 1"
Output: 2

Example 2:
Input: s = " 2-1 + 2 "
Output: 3

Example 3:
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
"""
def calculate(s):
    stack = []
    res = 0
    num = 0
    sign = 1
    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c in '+-':
            res += sign * num
            num = 0
            sign = 1 if c == '+' else -1
        elif c == '(': 
            stack.append(res)
            stack.append(sign)
            res = 0
            sign = 1
        elif c == ')':
            res += sign * num
            num = 0
            res *= stack.pop()
            res += stack.pop()
    res += sign * num
    return res

# Example usage:
if __name__ == "__main__":
    print(calculate("1 + 1"))            # Output: 2
    print(calculate(" 2-1 + 2 "))        # Output: 3
    print(calculate("(1+(4+5+2)-3)+(6+8)")) # Output: 23
