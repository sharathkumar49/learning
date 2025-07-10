"""
LeetCode 1694. Reformat Phone Number

Given a string number, reformat it to blocks of 2 or 3 digits separated by dashes.

Example 1:
Input: number = "1-23-45 6"
Output: "123-456"

Constraints:
- 2 <= number.length <= 100
- number consists of digits, spaces, and dashes.
"""

def reformatNumber(number):
    digits = [c for c in number if c.isdigit()]
    res = []
    i = 0
    n = len(digits)
    while n - i > 4:
        res.append(''.join(digits[i:i+3]))
        i += 3
    if n - i == 4:
        res.append(''.join(digits[i:i+2]))
        res.append(''.join(digits[i+2:i+4]))
    else:
        res.append(''.join(digits[i:]))
    return '-'.join(res)

# Example usage:
# number = "1-23-45 6"
# print(reformatNumber(number))  # Output: "123-456"
