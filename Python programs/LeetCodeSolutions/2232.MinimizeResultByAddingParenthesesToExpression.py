"""
LeetCode 2232. Minimize Result by Adding Parentheses to Expression

Given a string expression of the form "num1+num2", return the minimized result by adding parentheses.

Example:
Input: expression = "247+38"
Output: "2(47+3)8"

Constraints:
- 3 <= expression.length <= 10
- expression contains exactly one '+'
"""

def minimizeResult(expression):
    plus = expression.index('+')
    min_val = float('inf')
    res = ''
    for i in range(plus):
        for j in range(plus+2, len(expression)+1):
            left = int(expression[:i]) if i > 0 else 1
            mid_left = int(expression[i:plus])
            mid_right = int(expression[plus+1:j])
            right = int(expression[j:]) if j < len(expression) else 1
            val = left * (mid_left + mid_right) * right
            if val < min_val:
                min_val = val
                res = expression[:i] + '(' + expression[i:j] + ')' + expression[j:]
    return res

# Example usage:
# print(minimizeResult("247+38"))  # Output: "2(47+3)8"
