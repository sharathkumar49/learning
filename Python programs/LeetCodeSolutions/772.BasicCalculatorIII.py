"""
772. Basic Calculator III

Implement a basic calculator to evaluate a simple expression string containing non-negative integers, '+', '-', '*', '/', '(', ')', and empty spaces.

Example 1:
Input: s = "2*(5+5*2)/3+(6/2+8)"
Output: 21

Example 2:
Input: s = "(2+6* 3+5- (3*14/7+2)*5)+3"
Output: -12

Constraints:
- 1 <= s.length <= 10^4
- s consists of digits, '+', '-', '*', '/', '(', ')', and ' '.
- s is a valid expression.
"""
def calculate(s):
    def helper(it):
        num, stack, sign = 0, [], '+'
        while True:
            try:
                c = next(it)
            except StopIteration:
                break
            if c.isdigit():
                num = num * 10 + int(c)
            if c == '(': 
                num = helper(it)
            if (not c.isdigit() and c != ' ') or c == ')':
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] *= num
                elif sign == '/':
                    stack[-1] = int(stack[-1] / num)
                num = 0
                sign = c
            if c == ')':
                break
        return sum(stack)
    return helper(iter(s))

# Example usage:
print(calculate("2*(5+5*2)/3+(6/2+8)"))  # Output: 21
print(calculate("(2+6* 3+5- (3*14/7+2)*5)+3"))  # Output: -12
