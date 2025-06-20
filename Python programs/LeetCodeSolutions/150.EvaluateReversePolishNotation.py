"""
150. Evaluate Reverse Polish Notation
https://leetcode.com/problems/evaluate-reverse-polish-notation/

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Constraints:
- 1 <= tokens.length <= 10^4
- tokens[i] is either an operator: "+", "-", "*", "/", or an integer in the range [-200, 200].

Example:
Input: tokens = ["2","1","+","3","*"]
Output: 9
"""
from typing import List

def evalRPN(tokens: List[str]) -> int:
    stack = []
    for token in tokens:
        if token in {"+", "-", "*", "/"}:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            else:
                stack.append(int(a / b))
        else:
            stack.append(int(token))
    return stack[0]

# Example usage:
if __name__ == "__main__":
    print(evalRPN(["2","1","+","3","*"]))  # Output: 9
    print(evalRPN(["4","13","5","/","+"]))  # Output: 6
