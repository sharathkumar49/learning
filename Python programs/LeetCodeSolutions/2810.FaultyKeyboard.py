"""
LeetCode 2810. Faulty Keyboard

Given s, return the string after simulating the faulty keyboard.

Constraints:
- 1 <= s.length <= 100
"""

def finalString(s):
    res = []
    for c in s:
        if c == 'i':
            res.reverse()
        else:
            res.append(c)
    return ''.join(res)
# Example usage:
# print(finalString("string"))  # Output: (example)
