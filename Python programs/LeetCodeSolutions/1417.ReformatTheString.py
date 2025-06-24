"""
LeetCode 1417. Reformat The String

Given alphanumeric string s, return the string after reformatting it so that no two adjacent characters are of the same type. If it is not possible, return an empty string.

Constraints:
- 1 <= s.length <= 500
- s consists of only lowercase English letters and/or digits.

Example:
Input: s = "a0b1c2"
Output: "a0b1c2"
"""
def reformat(s):
    letters = [c for c in s if c.isalpha()]
    digits = [c for c in s if c.isdigit()]
    if abs(len(letters) - len(digits)) > 1:
        return ""
    res = []
    if len(letters) > len(digits):
        letters, digits = digits, letters
    for i in range(len(s)):
        if i % 2 == 0:
            res.append(digits.pop())
        else:
            res.append(letters.pop())
    return ''.join(res)

# Example usage:
s = "a0b1c2"
print(reformat(s))  # Output: "a0b1c2"
