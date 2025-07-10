"""
LeetCode 1796. Second Largest Digit in a String

Given a string s, return the second largest numerical digit in s, or -1 if it does not exist.

Example 1:
Input: s = "dfa12321afd"
Output: 2

Constraints:
- 1 <= s.length <= 500
- s consists of digits and lowercase English letters
"""

def secondHighest(s):
    digits = sorted({int(c) for c in s if c.isdigit()}, reverse=True)
    return digits[1] if len(digits) > 1 else -1

# Example usage:
# s = "dfa12321afd"
# print(secondHighest(s))  # Output: 2
