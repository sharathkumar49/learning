"""
LeetCode 1404. Number of Steps to Reduce a Number in Binary Representation to One

Given a binary string s, return the number of steps to reduce it to 1 under the following rules:
- If the current number is even, divide it by 2.
- If the current number is odd, add 1 to it.

Constraints:
- 1 <= s.length <= 500
- s consists only of '0' or '1'.

Example:
Input: s = "1101"
Output: 6
"""
def numSteps(s):
    s = list(s)
    steps = 0
    while len(s) > 1:
        if s[-1] == '0':
            s.pop()
        else:
            i = len(s) - 1
            while i >= 0 and s[i] == '1':
                s[i] = '0'
                i -= 1
            if i >= 0:
                s[i] = '1'
            else:
                s = ['1'] + s
        steps += 1
    return steps

# Example usage:
s = "1101"
print(numSteps(s))  # Output: 6
