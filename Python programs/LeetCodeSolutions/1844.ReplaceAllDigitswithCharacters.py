"""
LeetCode 1844. Replace All Digits with Characters

You are given a string s consisting of digits and lowercase English letters. Replace every digit in s with the character that comes after the previous character in the alphabet.

Example 1:
Input: s = "a1c1e1"
Output: "abcdef"

Constraints:
- 1 <= s.length <= 100
- s consists of lowercase English letters and digits.
"""

def replaceDigits(s):
    res = []
    for i, c in enumerate(s):
        if c.isdigit():
            res.append(chr(ord(s[i-1]) + int(c)))
        else:
            res.append(c)
    return ''.join(res)

# Example usage:
# s = "a1c1e1"
# print(replaceDigits(s))  # Output: "abcdef"
