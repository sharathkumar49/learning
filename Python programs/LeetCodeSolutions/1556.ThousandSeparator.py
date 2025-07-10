"""
LeetCode 1556. Thousand Separator

Given an integer n, return a string representing the integer with commas as thousand separators.

Constraints:
- 0 <= n <= 10^9

Example:
Input: n = 123456789
Output: "123,456,789"
"""
def thousandSeparator(n):
    s = str(n)
    res = ''
    for i, c in enumerate(reversed(s)):
        if i and i % 3 == 0:
            res = ',' + res
        res = c + res
    return res

# Example usage:
n = 123456789
print(thousandSeparator(n))  # Output: "123,456,789"
