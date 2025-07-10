"""
LeetCode 1678. Goal Parser Interpretation

Given a string command, interpret it as per the following rules:
- "G" -> "G"
- "()" -> "o"
- "(al)" -> "al"
Return the interpreted string.

Example 1:
Input: command = "G()(al)"
Output: "Goal"

Constraints:
- 1 <= command.length <= 100
- command consists of "G", "()", and/or "(al)" in some order.
"""

def interpret(command):
    return command.replace('()', 'o').replace('(al)', 'al')

# Example usage:
# command = "G()(al)"
# print(interpret(command))  # Output: "Goal"
