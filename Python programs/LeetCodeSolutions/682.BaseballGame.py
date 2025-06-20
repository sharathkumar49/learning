"""
LeetCode 682. Baseball Game

You are keeping score for a baseball game with strange rules. Each operation is a string:
- Integer x: Record a new score of x.
- "+": Record a new score that is the sum of the previous two scores.
- "D": Record a new score that is double the previous score.
- "C": Invalidate the previous score, removing it from the record.

Return the sum of all the scores on the record after all operations.

Example 1:
Input: ops = ["5","2","C","D","+"]
Output: 30
Explanation: [5,2] -> [5] -> [5,10] -> [5,10,15] = 30

Example 2:
Input: ops = ["5","-2","4","C","D","9","+","+"]
Output: 27

Constraints:
- 1 <= ops.length <= 1000
- ops[i] is "C", "D", "+", or a string representing an integer.
- It is guaranteed that every operation is valid.
"""
from typing import List

def calPoints(ops: List[str]) -> int:
    stack = []
    for op in ops:
        if op == '+':
            stack.append(stack[-1] + stack[-2])
        elif op == 'D':
            stack.append(2 * stack[-1])
        elif op == 'C':
            stack.pop()
        else:
            stack.append(int(op))
    return sum(stack)

# Example usage
if __name__ == "__main__":
    print(calPoints(["5","2","C","D","+"]))  # Output: 30
    print(calPoints(["5","-2","4","C","D","9","+","+"]))  # Output: 27
